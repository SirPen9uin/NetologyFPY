const book = document.getElementById('book');

const fontSizeSmallLink = document.querySelector('.font-size_small');
const fontSizeBigLink = document.querySelector('.font-size_big');

fontSizeSmallLink.addEventListener('click', event => {
  event.preventDefault();
  book.style.fontSize = 'small';
});

fontSizeBigLink.addEventListener('click', event => {
  event.preventDefault();
  book.style.fontSize = 'large';
});