const img = document.getElementById('cookie')
const clicker = document.getElementById('clicker__counter')
counter = 0
img.onclick = () => {
    if (counter % 2 === 0) {
        img.width += 20
        img.height += 20
        counter += 1
    } else {
        img.width -= 20
        img.height -= 20
        counter += 1
    }
    clicker.textContent = counter
}