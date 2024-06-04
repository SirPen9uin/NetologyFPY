const popup = document.querySelector('.modal');
const closeButton = document.querySelector('.modal__close');
console.log(document.cookie);

function setCookie(name, value) {
  document.cookie = `${name}=${value}; expires=Fri, 31 Dec 9999 23:59:59 GMT`;
}

function getCookie(name) {
  const pairs = document.cookie.split('; ');
  const cookie = pairs.find(p => p.startsWith(`${name}=`));
  return cookie ? cookie.substring(name.length + 1) : null;
}

// Проверяем, было ли окно уже показано в cookie
const wasShown = getCookie('wasShown') === 'true';

if (!wasShown) {
  // Если окно не было показано ранее, отображаем его
  popup.classList.add('modal_active');

  // Устанавливаем cookie для сохранения информации о том, что окно было показано
  setCookie('wasShown', 'true');
}

// Добавляем обработчик события для закрытия окна
closeButton.addEventListener('click', () => {
  popup.classList.remove('modal_active');
});