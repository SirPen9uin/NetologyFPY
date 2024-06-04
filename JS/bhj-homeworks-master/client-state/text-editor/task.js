const textarea = document.querySelector('textarea');
const storedText = localStorage.getItem('text');

if (storedText) {
  textarea.value = storedText;
}

textarea.addEventListener('input', () => {
  const text = textarea.value;
  localStorage.setItem('text', text);
});