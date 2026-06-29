const header = document.querySelector('[data-header]');

function syncHeader() {
  if (!header) return;
  header.classList.toggle('is-scrolled', window.scrollY > 16);
}

window.addEventListener('scroll', syncHeader, { passive: true });
syncHeader();

for (const button of document.querySelectorAll('[data-copy]')) {
  button.addEventListener('click', async () => {
    const text = button.getAttribute('data-copy') || '';
    try {
      await navigator.clipboard.writeText(text);
      const original = button.textContent;
      button.textContent = '已复制';
      window.setTimeout(() => {
        button.textContent = original;
      }, 1400);
    } catch {
      button.textContent = '复制失败';
    }
  });
}
