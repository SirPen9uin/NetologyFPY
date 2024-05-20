const reveals = document.querySelectorAll('.reveal');

function isVisible(el) {
  const {top, bottom} = el.getBoundingClientRect()

  if (bottom < 0) {
    return false
  }

  if (top > window.innerHeight) {
    return false
  }

  return true
}

reveals.forEach((reveal) => {
  setInterval(() => {
    console.log(isVisible(reveal))
    if (isVisible(reveal)) {
      reveal.classList.add('reveal_active');
    }

    if (!isVisible(reveal)) {
      reveal.classList.remove('reveal_active')
    }
  }, 500);
});

