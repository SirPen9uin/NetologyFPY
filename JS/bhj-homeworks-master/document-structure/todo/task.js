const form = document.getElementById('tasks__form');
const inputEl = document.getElementById('task__input');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const newEl = document.createElement('div');
  newEl.classList.add('task');
  newEl.innerHTML = `
    <div class="task__title"></div>
    <a href="#" class="task__remove">&times;</a>
  `;
  newEl.querySelector('.task__title').textContent = inputEl.value;
  newEl.querySelector('.task__remove').addEventListener('click', () => {
    newEl.remove();
  });
  document.getElementById('tasks__list').appendChild(newEl);
  inputEl.value = '';
});
