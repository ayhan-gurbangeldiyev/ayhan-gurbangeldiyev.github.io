/* Run before CSS to apply an explicit preference without a theme flash. */
(() => {
  try {
    const theme = localStorage.getItem('engineering-notes-theme');
    if (theme === 'dark' || theme === 'light') document.documentElement.dataset.theme = theme;
  } catch (_) { /* System preference remains usable when storage is unavailable. */ }
})();
