const tooltipsElements = document.querySelectorAll('.has-tooltip');
let newEl = document.createElement('div');
newEl.classList.add('tooltip');
let isClicked = false;
tooltipsElements.forEach((el) => {
  el.addEventListener('click', (e) => {
    e.preventDefault();
    if (isClicked) {
      newEl.remove();
      isClicked = false;
    } else {
      const top = el.getBoundingClientRect().top;
      const left = el.getBoundingClientRect().left;
      newEl.style.top = `${top + 20}px`;
      newEl.style.left = `${left}px`;
      const tooltipText = el.title;
      el.insertAdjacentElement('afterend', newEl);
      newEl.textContent = tooltipText;
      newEl.classList.add('tooltip_active');
      isClicked = true;
    }
  });
});