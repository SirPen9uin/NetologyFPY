const textarea = document.querySelector('textarea');
const storedText = localStorage.getItem('text');
const btn = document.getElementById('clear');

if (storedText) {
  textarea.value = storedText;
}

textarea.addEventListener('input', () => {
  const text = textarea.value;
  localStorage.setItem('text', text);
});

btn.addEventListener('click', () => {
  textarea.value = '';
  localStorage.removeItem('text');
})