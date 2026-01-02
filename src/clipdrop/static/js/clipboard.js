/**
 * Clipboard Module
 * Handles clipboard copy, share, and delete operations
 */

(function() {
    'use strict';

    /**
     * Copy text to clipboard
     * @param {string} text - Text to copy
     * @returns {Promise<boolean>} Success status
     */
    async function copyToClipboard(text) {
        try {
            await navigator.clipboard.writeText(text);
            return true;
        } catch (err) {
            // Fallback for older browsers
            const textarea = document.createElement('textarea');
            textarea.value = text;
            textarea.style.position = 'fixed';
            textarea.style.opacity = '0';
            document.body.appendChild(textarea);
            textarea.select();
            try {
                document.execCommand('copy');
                document.body.removeChild(textarea);
                return true;
            } catch (e) {
                document.body.removeChild(textarea);
                return false;
            }
        }
    }

    /**
     * Share content using Web Share API or fallback to copy
     * @param {Object} shareData - Share data object
     * @param {string} shareData.title - Share title
     * @param {string} shareData.text - Share text
     * @param {string} shareData.url - Share URL
     * @returns {Promise<boolean>} Success status
     */
    async function shareContent(shareData) {
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
            // Fallback: copy URL or text to clipboard
            const textToCopy = shareData.url || shareData.text || '';
            const success = await copyToClipboard(textToCopy);
            if (success && window.showToast) {
                window.showToast('Link copied to clipboard!', 'success');
            }
            return success;
        }
    }

    /**
     * Delete a clipboard item
     * @param {string|number} itemId - Item ID to delete
     * @returns {Promise<Object>} Response data
     */
    async function deleteClipboardItem(itemId) {
        const response = await fetch(`/clipboard/${itemId}/delete`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        return response.json();
    }

    /**
     * Initialize clipboard item event handlers
     * Call this after DOM is ready or after dynamic content is added
     */
    function initClipboardHandlers() {
        // Copy buttons
        document.querySelectorAll('.copy-btn').forEach(function(btn) {
            btn.addEventListener('click', async function() {
                const content = this.dataset.content;
                const success = await copyToClipboard(content);
                if (window.showToast) {
                    if (success) {
                        window.showToast('Copied to clipboard!', 'success');
                    } else {
                        window.showToast('Failed to copy to clipboard', 'error');
                    }
                }
            });
        });

        // Share buttons for clipboard items
        document.querySelectorAll('.clipboard-share-btn').forEach(function(btn) {
            btn.addEventListener('click', async function() {
                const content = this.dataset.content;
                const itemId = this.dataset.id;
                await shareContent({
                    title: 'Shared Clipboard Item',
                    text: content,
                    url: window.location.origin + '/clipboard/' + itemId
                });
            });
        });

        // Delete buttons for clipboard items
        document.querySelectorAll('.clipboard-delete-btn').forEach(function(btn) {
            btn.addEventListener('click', function() {
                const itemId = this.dataset.id;
                const row = this.closest('tr, .clipboard-item, .card');

                if (window.showConfirmModal) {
                    window.showConfirmModal({
                        title: 'Delete Clipboard Item',
                        message: 'Are you sure you want to delete this clipboard item? This action cannot be undone.',
                        confirmText: 'Delete',
                        confirmIcon: 'fa-trash',
                        onConfirm: async function() {
                            try {
                                const data = await deleteClipboardItem(itemId);
                                if (data.success) {
                                    if (row) row.remove();
                                    if (window.showToast) {
                                        window.showToast('Clipboard item deleted successfully', 'success');
                                    }
                                    // Check if table is empty
                                    const tableBody = document.querySelector('.clipboard-table tbody');
                                    if (tableBody && tableBody.children.length === 0) {
                                        location.reload();
                                    }
                                } else {
                                    if (window.showToast) {
                                        window.showToast(data.error || 'Failed to delete item', 'error');
                                    }
                                }
                            } catch (err) {
                                if (window.showToast) {
                                    window.showToast('Error deleting item', 'error');
                                }
                            }
                        }
                    });
                } else {
                    // Fallback to confirm dialog
                    if (confirm('Are you sure you want to delete this item?')) {
                        deleteClipboardItem(itemId).then(function(data) {
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
        document.addEventListener('DOMContentLoaded', initClipboardHandlers);
    } else {
        initClipboardHandlers();
    }

    // Export globally
    window.ClipDrop = window.ClipDrop || {};
    window.ClipDrop.clipboard = {
        copy: copyToClipboard,
        share: shareContent,
        deleteItem: deleteClipboardItem,
        init: initClipboardHandlers
    };
})();
