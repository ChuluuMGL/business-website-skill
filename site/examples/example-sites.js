const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!reduceMotion) {
  document.documentElement.classList.add('motion-ready');

  const revealItems = document.querySelectorAll('.card, .process-card, .scenario, .visual-panel, .final-cta');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      }
    }, { threshold: 0.14 });

    for (const item of revealItems) {
      observer.observe(item);
    }
  } else {
    for (const item of revealItems) {
      item.classList.add('is-visible');
    }
  }

  for (const hero of document.querySelectorAll('.hero-site')) {
    hero.addEventListener('pointermove', (event) => {
      const rect = hero.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width) * 100;
      const y = ((event.clientY - rect.top) / rect.height) * 100;
      hero.style.setProperty('--mx', `${x.toFixed(1)}%`);
      hero.style.setProperty('--my', `${y.toFixed(1)}%`);
    }, { passive: true });
  }
}
