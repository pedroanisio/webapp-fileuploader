#!/usr/bin/env python3
"""
Migrate clipboard tables from integer IDs to ULID string IDs (PostgreSQL only).

Usage:
  DATABASE_URL=postgresql+psycopg://... python scripts/migrate_clipboard_ulid.py
"""

import os
import sys

import ulid
from sqlalchemy import create_engine, text


def get_database_url() -> str:
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise SystemExit("DATABASE_URL is required to run this migration.")
    return db_url


def fetch_all(conn, query: str):
    return conn.execute(text(query)).mappings().all()


def main() -> int:
    db_url = get_database_url()
    engine = create_engine(db_url)
    if engine.dialect.name != "postgresql":
        print("This migration script only supports PostgreSQL.")
        return 1

    with engine.begin() as conn:
        table_exists = conn.execute(text("SELECT to_regclass('public.clipboard_item')")).scalar()
        if not table_exists:
            print("No clipboard tables found. Nothing to migrate.")
            return 0

        id_type = conn.execute(
            text(
                """
                SELECT data_type
                FROM information_schema.columns
                WHERE table_name = 'clipboard_item' AND column_name = 'id'
                """
            )
        ).scalar()
        if id_type in ("character varying", "text"):
            print("Clipboard tables already use string IDs. Nothing to migrate.")
            return 0

        folders = fetch_all(
            conn,
            """
            SELECT id, user_id, name, parent_id, created_at, updated_at
            FROM clipboard_folder
            """,
        )
        items = fetch_all(
            conn,
            """
            SELECT id, user_id, folder_id, name, content, content_type, is_text,
                   size, favorite, created_at, updated_at, expires_at
            FROM clipboard_item
            """,
        )
        item_tags = fetch_all(
            conn,
            "SELECT item_id, tag_id FROM clipboard_item_tags",
        )

        folder_map = {row["id"]: str(ulid.new()) for row in folders}
        item_map = {row["id"]: str(ulid.new()) for row in items}

        conn.execute(text("DROP TABLE IF EXISTS clipboard_item_tags_new"))
        conn.execute(text("DROP TABLE IF EXISTS clipboard_item_new"))
        conn.execute(text("DROP TABLE IF EXISTS clipboard_folder_new"))

        conn.execute(
            text(
                """
                CREATE TABLE clipboard_folder_new (
                    id VARCHAR(26) PRIMARY KEY,
                    user_id INTEGER NOT NULL REFERENCES "user"(id),
                    name VARCHAR(255) NOT NULL,
                    parent_id VARCHAR(26) REFERENCES clipboard_folder_new(id),
                    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                    updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                    UNIQUE (user_id, parent_id, name)
                )
                """
            )
        )

        conn.execute(
            text(
                """
                CREATE TABLE clipboard_item_new (
                    id VARCHAR(26) PRIMARY KEY,
                    user_id INTEGER NOT NULL REFERENCES "user"(id),
                    folder_id VARCHAR(26) REFERENCES clipboard_folder_new(id),
                    name VARCHAR(255) NOT NULL,
                    content BYTEA NOT NULL,
                    content_type VARCHAR(255) NOT NULL,
                    is_text BOOLEAN NOT NULL,
                    size INTEGER NOT NULL,
                    favorite BOOLEAN NOT NULL,
                    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                    updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                    expires_at TIMESTAMP WITHOUT TIME ZONE
                )
                """
            )
        )

        conn.execute(
            text(
                """
                CREATE TABLE clipboard_item_tags_new (
                    item_id VARCHAR(26) NOT NULL REFERENCES clipboard_item_new(id) ON DELETE CASCADE,
                    tag_id INTEGER NOT NULL REFERENCES clipboard_tag(id) ON DELETE CASCADE,
                    PRIMARY KEY (item_id, tag_id)
                )
                """
            )
        )

        for row in folders:
            conn.execute(
                text(
                    """
                    INSERT INTO clipboard_folder_new (
                        id, user_id, name, parent_id, created_at, updated_at
                    ) VALUES (
                        :id, :user_id, :name, :parent_id, :created_at, :updated_at
                    )
                    """
                ),
                {
                    "id": folder_map[row["id"]],
                    "user_id": row["user_id"],
                    "name": row["name"],
                    "parent_id": folder_map.get(row["parent_id"]),
                    "created_at": row["created_at"],
                    "updated_at": row["updated_at"],
                },
            )

        for row in items:
            conn.execute(
                text(
                    """
                    INSERT INTO clipboard_item_new (
                        id, user_id, folder_id, name, content, content_type, is_text,
                        size, favorite, created_at, updated_at, expires_at
                    ) VALUES (
                        :id, :user_id, :folder_id, :name, :content, :content_type, :is_text,
                        :size, :favorite, :created_at, :updated_at, :expires_at
                    )
                    """
                ),
                {
                    "id": item_map[row["id"]],
                    "user_id": row["user_id"],
                    "folder_id": folder_map.get(row["folder_id"]),
                    "name": row["name"],
                    "content": row["content"],
                    "content_type": row["content_type"],
                    "is_text": row["is_text"],
                    "size": row["size"],
                    "favorite": row["favorite"],
                    "created_at": row["created_at"],
                    "updated_at": row["updated_at"],
                    "expires_at": row["expires_at"],
                },
            )

        for row in item_tags:
            new_item_id = item_map.get(row["item_id"])
            if not new_item_id:
                continue
            conn.execute(
                text(
                    """
                    INSERT INTO clipboard_item_tags_new (item_id, tag_id)
                    VALUES (:item_id, :tag_id)
                    """
                ),
                {"item_id": new_item_id, "tag_id": row["tag_id"]},
            )

        conn.execute(text("DROP TABLE IF EXISTS clipboard_item_tags"))
        conn.execute(text("DROP TABLE IF EXISTS clipboard_item"))
        conn.execute(text("DROP TABLE IF EXISTS clipboard_folder"))

        conn.execute(text("ALTER TABLE clipboard_folder_new RENAME TO clipboard_folder"))
        conn.execute(text("ALTER TABLE clipboard_item_new RENAME TO clipboard_item"))
        conn.execute(text("ALTER TABLE clipboard_item_tags_new RENAME TO clipboard_item_tags"))

        conn.execute(
            text("CREATE INDEX ix_clipboard_item_user_folder ON clipboard_item (user_id, folder_id)")
        )
        conn.execute(
            text("CREATE INDEX ix_clipboard_item_user_favorite ON clipboard_item (user_id, favorite)")
        )

    print("Clipboard ULID migration complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
