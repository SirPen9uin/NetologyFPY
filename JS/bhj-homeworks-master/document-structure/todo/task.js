const baseEl = document.createElement('div');
baseEl.classList.add('task');
baseEl.innerHTML = `
  <div class="task__title"></div>
  <a href="#" class="task__remove">&times;</a>
`;
const inputEl = document.getElementById('task__input');

inputEl.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && e.target.value.trim() !== '') {
    const newEl = baseEl.cloneNode(true);
    newEl.querySelector('.task__title').textContent = e.target.value;
    newEl.querySelector('.task__remove').addEventListener('click', () => {
      newEl.remove();
    });
    document.getElementById('tasks__list').appendChild(newEl);
    e.target.value = '';
  }
});