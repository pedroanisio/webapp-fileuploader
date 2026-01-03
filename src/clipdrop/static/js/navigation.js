/**
 * Navigation Module
 * Handles mobile navigation drawer functionality
 */

(function() {
    'use strict';

    const mobileToggle = document.querySelector('.nav-mobile-toggle');
    const mobileNav = document.getElementById('mobile-nav');
    const mobileBackdrop = document.getElementById('mobile-nav-backdrop');
    const mobileClose = document.getElementById('mobile-nav-close');

    // Exit if navigation elements don't exist (e.g., on login page)
    if (!mobileToggle || !mobileNav) return;

    /**
     * Toggle mobile navigation drawer
     */
    function toggleMobileNav() {
        const isOpen = mobileNav.classList.contains('is-open');
        mobileNav.classList.toggle('is-open');
        mobileBackdrop.classList.toggle('is-visible');
        mobileToggle.setAttribute('aria-expanded', !isOpen);
        mobileToggle.setAttribute('aria-label', isOpen ? 'Open menu' : 'Close menu');

        if (!isOpen) {
            document.body.style.overflow = 'hidden';
            const firstLink = mobileNav.querySelector('.mobile-nav-link');
            if (firstLink) firstLink.focus();
        } else {
            document.body.style.overflow = '';
            mobileToggle.focus();
        }
    }

    /**
     * Close mobile navigation
     */
    function closeMobileNav() {
        if (mobileNav.classList.contains('is-open')) {
            toggleMobileNav();
        }
    }

    // Event listeners
    mobileToggle.addEventListener('click', toggleMobileNav);
    if (mobileBackdrop) mobileBackdrop.addEventListener('click', toggleMobileNav);
    if (mobileClose) mobileClose.addEventListener('click', toggleMobileNav);

    // Close on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && mobileNav.classList.contains('is-open')) {
            toggleMobileNav();
        }
    });

    // Export for external usage
    window.ClipDrop = window.ClipDrop || {};
    window.ClipDrop.navigation = {
        toggle: toggleMobileNav,
        close: closeMobileNav
    };

    /**
     * Action Dropdown Menu Handler
     * Handles mobile action dropdown menus
     */
    function initActionDropdowns() {
        document.addEventListener('click', function(e) {
            const toggle = e.target.closest('.action-dropdown-toggle');
            const dropdown = e.target.closest('.action-dropdown');

            // Close all dropdowns if clicking outside
            if (!dropdown) {
                document.querySelectorAll('.action-dropdown.is-open').forEach(function(d) {
                    d.classList.remove('is-open');
                    d.querySelector('.action-dropdown-toggle').setAttribute('aria-expanded', 'false');
                });
                return;
            }

            // Toggle clicked dropdown
            if (toggle) {
                e.preventDefault();
                e.stopPropagation();

                const isOpen = dropdown.classList.contains('is-open');

                // Close all other dropdowns first
                document.querySelectorAll('.action-dropdown.is-open').forEach(function(d) {
                    if (d !== dropdown) {
                        d.classList.remove('is-open');
                        d.querySelector('.action-dropdown-toggle').setAttribute('aria-expanded', 'false');
                    }
                });

                // Toggle current dropdown
                dropdown.classList.toggle('is-open');
                toggle.setAttribute('aria-expanded', !isOpen);
            }
        });

        // Close dropdowns on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                document.querySelectorAll('.action-dropdown.is-open').forEach(function(d) {
                    d.classList.remove('is-open');
                    d.querySelector('.action-dropdown-toggle').setAttribute('aria-expanded', 'false');
                });
            }
        });
    }

    // Initialize action dropdowns
    initActionDropdowns();
})();
