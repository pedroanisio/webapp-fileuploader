/**
 * Confirmation Modal Module
 * Handles confirmation dialogs for destructive actions
 */

(function() {
    'use strict';

    // Modal elements
    const confirmModal = document.getElementById('confirm-modal');
    const confirmModalBackdrop = document.getElementById('confirm-modal-backdrop');
    const confirmModalTitle = document.getElementById('confirm-modal-title');
    const confirmModalMessage = document.getElementById('confirm-modal-message');
    const confirmModalClose = document.getElementById('confirm-modal-close');
    const confirmModalCancel = document.getElementById('confirm-modal-cancel');
    const confirmModalConfirm = document.getElementById('confirm-modal-confirm');

    // Exit if modal elements don't exist
    if (!confirmModal) return;

    let confirmCallback = null;
    let previousActiveElement = null;

    /**
     * Show the confirmation modal
     * @param {Object} options - Modal options
     * @param {string} options.title - Modal title
     * @param {string} options.message - Modal message
     * @param {string} options.confirmText - Confirm button text
     * @param {string} options.confirmIcon - Confirm button icon class
     * @param {Function} options.onConfirm - Callback when confirmed
     */
    function showConfirmModal(options = {}) {
        const {
            title = 'Confirm Delete',
            message = 'Are you sure you want to delete this item? This action cannot be undone.',
            confirmText = 'Delete',
            confirmIcon = 'fa-trash',
            onConfirm = null
        } = options;

        previousActiveElement = document.activeElement;
        confirmModalTitle.textContent = title;
        confirmModalMessage.textContent = message;
        confirmModalConfirm.querySelector('span').textContent = confirmText;
        confirmModalConfirm.querySelector('i').className = `fas ${confirmIcon}`;
        confirmCallback = onConfirm;

        confirmModal.classList.add('is-visible');
        confirmModalBackdrop.classList.add('is-visible');
        document.body.style.overflow = 'hidden';
        confirmModalConfirm.focus();
    }

    /**
     * Hide the confirmation modal
     */
    function hideConfirmModal() {
        confirmModal.classList.remove('is-visible');
        confirmModalBackdrop.classList.remove('is-visible');
        document.body.style.overflow = '';
        confirmCallback = null;
        if (previousActiveElement) {
            previousActiveElement.focus();
        }
    }

    // Event listeners
    if (confirmModalClose) confirmModalClose.addEventListener('click', hideConfirmModal);
    if (confirmModalCancel) confirmModalCancel.addEventListener('click', hideConfirmModal);
    if (confirmModalBackdrop) confirmModalBackdrop.addEventListener('click', hideConfirmModal);

    if (confirmModalConfirm) {
        confirmModalConfirm.addEventListener('click', function() {
            if (confirmCallback) {
                confirmCallback();
            }
            hideConfirmModal();
        });
    }

    // Close on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && confirmModal.classList.contains('is-visible')) {
            hideConfirmModal();
        }
    });

    // Focus trap for modal
    confirmModal.addEventListener('keydown', function(e) {
        if (e.key !== 'Tab') return;

        const focusable = confirmModal.querySelectorAll('button:not([disabled])');
        const first = focusable[0];
        const last = focusable[focusable.length - 1];

        if (e.shiftKey && document.activeElement === first) {
            e.preventDefault();
            last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
            e.preventDefault();
            first.focus();
        }
    });

    // Export globally
    window.showConfirmModal = showConfirmModal;
    window.hideConfirmModal = hideConfirmModal;
    window.ClipDrop = window.ClipDrop || {};
    window.ClipDrop.modal = {
        show: showConfirmModal,
        hide: hideConfirmModal
    };
})();
