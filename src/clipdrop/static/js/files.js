/**
 * Files Module
 * Handles file upload, share, and delete operations
 */

(function() {
    'use strict';

    /**
     * Share a file using Web Share API or fallback to copy
     * @param {string} filename - File name
     * @param {string} url - Download URL
     * @returns {Promise<boolean>} Success status
     */
    async function shareFile(filename, url) {
        const shareData = {
            title: filename,
            text: `Check out this file: ${filename}`,
            url: url
        };

        if (navigator.share) {
            try {
                await navigator.share(shareData);
                return true;
            } catch (err) {
                if (err.name !== 'AbortError') {
                    console.error('Share failed:', err);
                }
                return false;
            }
        } else {
            // Fallback: copy URL to clipboard
            if (window.ClipDrop && window.ClipDrop.clipboard) {
                const success = await window.ClipDrop.clipboard.copy(url);
                if (success && window.showToast) {
                    window.showToast('Link copied to clipboard!', 'success');
                }
                return success;
            }
            return false;
        }
    }

    /**
     * Delete a file
     * @param {string} filename - Filename to delete
     * @returns {Promise<Object>} Response data
     */
    async function deleteFile(filename) {
        const response = await fetch(`/delete/${encodeURIComponent(filename)}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        return response.json();
    }

    /**
     * Initialize file action event handlers
     */
    function initFileHandlers() {
        // Share buttons for files
        document.querySelectorAll('.share-btn').forEach(function(btn) {
            btn.addEventListener('click', async function() {
                const filename = this.dataset.filename;
                const url = this.dataset.url;
                await shareFile(filename, url);
            });
        });

        // Delete buttons for files
        document.querySelectorAll('.delete-btn').forEach(function(btn) {
            btn.addEventListener('click', function() {
                const filename = this.dataset.filename;
                const row = this.closest('tr, .file-item, .card');

                if (window.showConfirmModal) {
                    window.showConfirmModal({
                        title: 'Delete File',
                        message: `Are you sure you want to delete "${filename}"? This action cannot be undone.`,
                        confirmText: 'Delete',
                        confirmIcon: 'fa-trash',
                        onConfirm: async function() {
                            try {
                                const data = await deleteFile(filename);
                                if (data.success) {
                                    if (row) row.remove();
                                    if (window.showToast) {
                                        window.showToast('File deleted successfully', 'success');
                                    }
                                    // Check if table is empty
                                    const tableBody = document.querySelector('.files-table tbody');
                                    if (tableBody && tableBody.children.length === 0) {
                                        location.reload();
                                    }
                                } else {
                                    if (window.showToast) {
                                        window.showToast(data.error || 'Failed to delete file', 'error');
                                    }
                                }
                            } catch (err) {
                                if (window.showToast) {
                                    window.showToast('Error deleting file', 'error');
                                }
                            }
                        }
                    });
                } else {
                    // Fallback to confirm dialog
                    if (confirm(`Are you sure you want to delete "${filename}"?`)) {
                        deleteFile(filename).then(function(data) {
                            if (data.success) {
                                if (row) row.remove();
                                location.reload();
                            }
                        });
                    }
                }
            });
        });
    }

    // Initialize on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initFileHandlers);
    } else {
        initFileHandlers();
    }

    // Export globally
    window.ClipDrop = window.ClipDrop || {};
    window.ClipDrop.files = {
        share: shareFile,
        deleteFile: deleteFile,
        init: initFileHandlers
    };
})();
