const timer = document.getElementById('timer');
let totalSeconds = 10;
let hours = 0;
let minutes = 0;
let seconds = 0;

const interval = setInterval(() => {
    if (totalSeconds > 0) {
        totalSeconds--;

        hours = Math.floor(totalSeconds / 3600);
        minutes = Math.floor((totalSeconds % 3600) / 60);
        seconds = totalSeconds % 60;

        timer.textContent = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    } else {
        clearInterval(interval);
        downloadFile('https://ru.pinterest.com/pin/324188873189748708/');
    }
}, 1000);

function downloadFile(url) {
    fetch(url)
        .then(response => response.blob())
        .then(blob => {
            const url = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = 'image.png';
            link.click();
            URL.revokeObjectURL(url);
        })
        .catch(error => console.error(error));
}