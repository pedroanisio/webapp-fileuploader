/**
 * Theme Module
 * Handles light/dark theme initialization and toggling
 */

(function initTheme() {
    const saved = localStorage.getItem('theme');
    const preferred = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', saved || preferred);
})();

/**
 * Toggle between light and dark themes
 */
function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    if (window.showToast) {
        window.showToast(`${next.charAt(0).toUpperCase() + next.slice(1)} mode`, 'info');
    }
}

/**
 * Set a specific theme
 * @param {string} theme - 'light' or 'dark'
 */
function setTheme(theme) {
    if (theme === 'light' || theme === 'dark') {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
    }
}

/**
 * Keyboard Shortcuts Module
 * Global keyboard shortcuts for power users
 */
(function initKeyboardShortcuts() {
    'use strict';

    document.addEventListener('keydown', function(e) {
        // Don't trigger shortcuts when typing in inputs
        const target = e.target;
        const isInput = target.tagName === 'INPUT' ||
                       target.tagName === 'TEXTAREA' ||
                       target.tagName === 'SELECT' ||
                       target.isContentEditable;

        if (isInput) return;

        // Cmd/Ctrl + key shortcuts
        const isMod = e.metaKey || e.ctrlKey;

        // ? or / - Show keyboard shortcuts help
        if ((e.key === '?' || (e.key === '/' && e.shiftKey)) && !isMod) {
            e.preventDefault();
            showShortcutsHelp();
            return;
        }

        // g + f - Go to Files (press g then f within 1 second)
        // g + c - Go to Clipboard
        if (e.key === 'g' && !isMod) {
            waitForSecondKey(['f', 'c'], function(secondKey) {
                if (secondKey === 'f') {
                    window.location.href = '/';
                } else if (secondKey === 'c') {
                    window.location.href = '/clipboard';
                }
            });
            return;
        }

        // t - Toggle theme
        if (e.key === 't' && !isMod && !e.shiftKey) {
            e.preventDefault();
            toggleTheme();
            return;
        }

        // n - New (focus on text input for quick paste or file upload)
        if (e.key === 'n' && !isMod) {
            e.preventDefault();
            const clipboardInput = document.getElementById('clipboard-text');
            const fileInput = document.getElementById('drag-drop-area');
            if (clipboardInput) {
                clipboardInput.focus();
            } else if (fileInput) {
                fileInput.click();
            }
            return;
        }
    });

    let pendingKey = null;
    let pendingTimeout = null;

    function waitForSecondKey(validKeys, callback) {
        if (pendingTimeout) {
            clearTimeout(pendingTimeout);
        }

        pendingKey = { validKeys, callback };

        function handleSecondKey(e) {
            if (pendingKey && pendingKey.validKeys.includes(e.key)) {
                e.preventDefault();
                pendingKey.callback(e.key);
            }
            cleanup();
        }

        function cleanup() {
            document.removeEventListener('keydown', handleSecondKey);
            pendingKey = null;
            if (pendingTimeout) {
                clearTimeout(pendingTimeout);
                pendingTimeout = null;
            }
        }

        document.addEventListener('keydown', handleSecondKey, { once: true });
        pendingTimeout = setTimeout(cleanup, 1000);
    }

    function showShortcutsHelp() {
        // Create modal if it doesn't exist
        let modal = document.getElementById('shortcuts-modal');
        if (!modal) {
            modal = document.createElement('div');
            modal.id = 'shortcuts-modal';
            modal.className = 'shortcuts-modal';
            modal.innerHTML = `
                <div class="shortcuts-modal-backdrop"></div>
                <div class="shortcuts-modal-content" role="dialog" aria-modal="true" aria-labelledby="shortcuts-title">
                    <div class="shortcuts-modal-header">
                        <h3 id="shortcuts-title"><i class="fas fa-keyboard" aria-hidden="true"></i> Keyboard Shortcuts</h3>
                        <button class="shortcuts-close" aria-label="Close">&times;</button>
                    </div>
                    <div class="shortcuts-modal-body">
                        <div class="shortcuts-section">
                            <h4>Navigation</h4>
                            <div class="shortcut-item">
                                <span class="shortcut-keys"><kbd>g</kbd> then <kbd>f</kbd></span>
                                <span class="shortcut-desc">Go to Files</span>
                            </div>
                            <div class="shortcut-item">
                                <span class="shortcut-keys"><kbd>g</kbd> then <kbd>c</kbd></span>
                                <span class="shortcut-desc">Go to Clipboard</span>
                            </div>
                        </div>
                        <div class="shortcuts-section">
                            <h4>Actions</h4>
                            <div class="shortcut-item">
                                <span class="shortcut-keys"><kbd>n</kbd></span>
                                <span class="shortcut-desc">New item / Upload</span>
                            </div>
                            <div class="shortcut-item">
                                <span class="shortcut-keys"><kbd>t</kbd></span>
                                <span class="shortcut-desc">Toggle dark mode</span>
                            </div>
                            <div class="shortcut-item">
                                <span class="shortcut-keys"><kbd>?</kbd></span>
                                <span class="shortcut-desc">Show this help</span>
                            </div>
                        </div>
                    </div>
                </div>
            `;
            document.body.appendChild(modal);

            // Close handlers
            modal.querySelector('.shortcuts-close').addEventListener('click', hideShortcutsHelp);
            modal.querySelector('.shortcuts-modal-backdrop').addEventListener('click', hideShortcutsHelp);
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Escape' && modal.classList.contains('is-visible')) {
                    hideShortcutsHelp();
                }
            });
        }

        modal.classList.add('is-visible');
        document.body.style.overflow = 'hidden';
    }

    function hideShortcutsHelp() {
        const modal = document.getElementById('shortcuts-modal');
        if (modal) {
            modal.classList.remove('is-visible');
            document.body.style.overflow = '';
        }
    }

    // Export
    window.showShortcutsHelp = showShortcutsHelp;
    window.hideShortcutsHelp = hideShortcutsHelp;
})();

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { toggleTheme, setTheme };
}
