const timer = document.getElementById('timer')

setInterval(() => {
    if (timer.textContent != 0) {
        timer.textContent = Number(timer.textContent) - 1
    }
}, 1000)
