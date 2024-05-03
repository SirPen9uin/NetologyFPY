const img = document.getElementById('cookie')
const clicker = document.getElementById('clicker__counter')
const speed = document.getElementById('clicker__speed')
counter = 0
let lastClickTime = 0;

img.onclick = () => {
    const currentTime = new Date().getTime();
    const timeDifference = currentTime - lastClickTime;
    const clickSpeed = 1000 / timeDifference;
    lastClickTime = currentTime;
    
    speed.textContent = clickSpeed.toFixed(2);
    
    if (counter % 2 === 0) {
        img.width += 20;
        img.height += 20;
        counter += 1;
    } else {
        img.width -= 20;
        img.height -= 20;
        counter += 1;
    }
    clicker.textContent = counter;
};