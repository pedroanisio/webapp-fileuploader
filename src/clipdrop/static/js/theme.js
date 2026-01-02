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

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { toggleTheme, setTheme };
}
