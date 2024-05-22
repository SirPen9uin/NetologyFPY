const book = document.getElementById('book');

const fontSizeSmallLink = document.querySelector('.font-size_small');
const fontSizeBigLink = document.querySelector('.font-size_big');
const fontSizeActiveLink = document.querySelector('.font-size_active');

fontSizeSmallLink.addEventListener('click', event => {
  event.preventDefault();
  book.style.fontSize = 'small';
  fontSizeActiveLink.classList.remove('font-size_active');
  fontSizeBigLink.classList.remove('font-size_active');
  fontSizeSmallLink.classList.add('font-size_active');
});

fontSizeBigLink.addEventListener('click', event => {
  event.preventDefault();
  book.style.fontSize = 'large';
  fontSizeActiveLink.classList.remove('font-size_active');
  fontSizeSmallLink.classList.remove('font-size_active');
  fontSizeBigLink.classList.add('font-size_active');
});

fontSizeActiveLink.addEventListener('click', event => {
  event.preventDefault();
  book.style.fontSize = 'medium';
  fontSizeSmallLink.classList.remove('font-size_active');
  fontSizeBigLink.classList.remove('font-size_active');
  fontSizeActiveLink.classList.add('font-size_active');
});

// Повышенный уровень сложности

const textBlackLink = document.querySelector('.text_color_black');
const textGrayLink = document.querySelector('.text_color_gray');
const textWhitesmokeLink = document.querySelector('.text_color_whitesmoke');

textBlackLink.addEventListener('click', event => {
  event.preventDefault();
  book.style.color = 'black';
  textGrayLink.classList.remove('color_active');
  textWhitesmokeLink.classList.remove('color_active');
  textBlackLink.classList.add('color_active');
});

textGrayLink.addEventListener('click', event => {
  event.preventDefault();
  book.style.color = 'gray';
  textBlackLink.classList.remove('color_active');
  textWhitesmokeLink.classList.remove('color_active');
  textGrayLink.classList.add('color_active');
});

textWhitesmokeLink.addEventListener('click', event => {
  event.preventDefault(); 
  book.style.color = 'whitesmoke';
  textBlackLink.classList.remove('color_active');
  textGrayLink.classList.remove('color_active');
  textWhitesmokeLink.classList.add('color_active');
});

const bgBlackLink = document.querySelector('.bg_color_black');
const bgGrayLink = document.querySelector('.bg_color_gray');
const bgWhiteLink = document.querySelector('.bg_color_white');

bgBlackLink.addEventListener('click', event => {
  event.preventDefault();
  book.style.backgroundColor = 'black';
  bgGrayLink.classList.remove('color_active');
  bgWhiteLink.classList.remove('color_active');
  bgBlackLink.classList.add('color_active');
});

bgGrayLink.addEventListener('click', event => {
  event.preventDefault();
  book.style.backgroundColor = 'gray';
  bgBlackLink.classList.remove('color_active');
  bgWhiteLink.classList.remove('color_active');
  bgGrayLink.classList.add('color_active');
});

bgWhiteLink.addEventListener('click', event => {
  event.preventDefault();
  book.style.backgroundColor = 'white';
  bgBlackLink.classList.remove('color_active');
  bgGrayLink.classList.remove('color_active');
  bgWhiteLink.classList.add('color_active');
});