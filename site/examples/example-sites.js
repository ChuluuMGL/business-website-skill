const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!reduceMotion) {
  document.documentElement.classList.add('motion-ready');

  const revealItems = document.querySelectorAll('.reveal');
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

  for (const hero of document.querySelectorAll('.b2b-hero, .industrial-hero, .ai-hero')) {
    hero.addEventListener('pointermove', (event) => {
      const rect = hero.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width) * 100;
      const y = ((event.clientY - rect.top) / rect.height) * 100;
      hero.style.setProperty('--mx', `${x.toFixed(1)}%`);
      hero.style.setProperty('--my', `${y.toFixed(1)}%`);
    }, { passive: true });
  }
}

function wireToggleGroup(root, buttonSelector, panelSelector, buttonAttr, panelAttr) {
  const buttons = Array.from(root.querySelectorAll(buttonSelector));
  const panels = Array.from(root.querySelectorAll(panelSelector));

  const activate = (button) => {
    const target = button.getAttribute(buttonAttr);
    if (!target) return;

    root.dataset.active = target;

    for (const item of buttons) {
      const active = item === button;
      item.classList.toggle('is-active', active);
      item.setAttribute('aria-selected', active ? 'true' : 'false');
    }

    for (const panel of panels) {
      const active = panel.getAttribute(panelAttr) === target;
      panel.classList.toggle('is-active', active);
      panel.setAttribute('aria-hidden', active ? 'false' : 'true');
    }
  };

  const initialButton = buttons.find((button) => button.classList.contains('is-active')) || buttons[0];
  if (initialButton) {
    activate(initialButton);
  }

  for (const button of buttons) {
    button.addEventListener('click', () => {
      activate(button);
    });
  }
}

for (const stepper of document.querySelectorAll('[data-stepper]')) {
  wireToggleGroup(stepper, '[data-step-button]', '[data-step-panel]', 'data-step-button', 'data-step-panel');
}

for (const tabs of document.querySelectorAll('[data-tabs]')) {
  wireToggleGroup(tabs, '[data-tab-button]', '[data-tab-panel]', 'data-tab-button', 'data-tab-panel');
}

for (const command of document.querySelectorAll('[data-command-states]')) {
  wireToggleGroup(command, '[data-command-button]', '[data-command-panel]', 'data-command-button', 'data-command-panel');
}
