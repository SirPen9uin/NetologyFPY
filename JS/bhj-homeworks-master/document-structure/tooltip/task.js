const tooltipsElements = document.querySelectorAll('.has-tooltip');
let activeTooltip = null;

tooltipsElements.forEach((el) => {
  el.addEventListener('click', (e) => {
    e.preventDefault();
    
    const linkText = el.textContent;
    const tooltipText = el.title;
    
    if (activeTooltip && activeTooltip.dataset.linkText === linkText) {
      activeTooltip.classList.toggle('tooltip_active');
    } else {
      if (activeTooltip) {
        activeTooltip.classList.remove('tooltip_active');
      }
      
      const top = el.getBoundingClientRect().top;
      const left = el.getBoundingClientRect().left;
      
      const newEl = document.createElement('div');
      newEl.classList.add('tooltip');
      newEl.dataset.linkText = linkText;
      newEl.style.top = `${top + 20}px`;
      newEl.style.left = `${left}px`;
      newEl.textContent = tooltipText;
      el.insertAdjacentElement('afterend', newEl);
      newEl.classList.add('tooltip_active');
      
      activeTooltip = newEl;

      document.addEventListener('click', (e) => {
        if (activeTooltip && !e.target.closest('.has-tooltip')) {
          activeTooltip.classList.remove('tooltip_active');
          activeTooltip = null;
        }
      });
    }
  });
});