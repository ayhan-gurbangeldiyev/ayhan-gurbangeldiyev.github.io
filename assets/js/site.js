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

  const feedAddress = document.getElementById('feed-address');
  const copyFeed = document.getElementById('copy-feed');
  const copyStatus = document.getElementById('copy-feed-status');
  if (feedAddress && copyFeed && copyStatus) {
    copyFeed.hidden = false;
    copyFeed.addEventListener('click', async () => {
      copyStatus.textContent = '';
      copyFeed.disabled = true;
      try {
        if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(feedAddress.value);
        copyStatus.textContent = 'Feed URL copied. Paste it into your RSS reader.';
      } catch (_) {
        feedAddress.focus();
        feedAddress.select();
        copyStatus.textContent = 'Select and copy the feed address above, then paste it into your reader.';
      } finally {
        copyFeed.disabled = false;
      }
    });
  }

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
