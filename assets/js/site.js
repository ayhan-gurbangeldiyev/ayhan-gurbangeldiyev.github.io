(() => {
  const themeSelect = document.getElementById('theme-select');
  if (themeSelect) {
    themeSelect.closest('label').hidden = false;
    themeSelect.value = document.documentElement.dataset.theme || 'system';
    themeSelect.addEventListener('change', () => {
      const theme = themeSelect.value;
      if (theme === 'system') delete document.documentElement.dataset.theme;
      else document.documentElement.dataset.theme = theme;
      try {
        if (theme === 'system') localStorage.removeItem('engineering-notes-theme');
        else localStorage.setItem('engineering-notes-theme', theme);
      } catch (_) { /* The current document can still change theme. */ }
    });
  }

  document.querySelectorAll('.article-content h2[id], .article-content h3[id]').forEach(heading => {
    const link = document.createElement('a');
    link.className = 'heading-anchor';
    link.href = '#' + heading.id;
    link.setAttribute('aria-label', 'Link to section: ' + heading.textContent);
    link.textContent = '#';
    heading.append(' ', link);
  });

  const search = document.getElementById('writing-search');
  if (search) {
    search.closest('label').hidden = false;
    const rows = [...document.querySelectorAll('[data-note]')];
    const status = document.getElementById('search-status');
    search.addEventListener('input', () => {
      const query = search.value.trim().toLowerCase();
      const terms = query.split(/\s+/).filter(Boolean);
      let count = 0;
      rows.forEach(row => {
        row.hidden = !terms.every(term => row.dataset.search.includes(term));
        if (!row.hidden) count++;
      });
      status.hidden = !query;
      status.textContent = count ? count + (count === 1 ? ' note found.' : ' notes found.') : 'No notes match. Try another title or topic.';
    });
  }
})();
