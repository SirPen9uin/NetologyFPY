const ads = document.querySelectorAll('.rotator__case');

function rotate() {
    for (let i = 0; i < ads.length; i++) {
        let speed = ads[i].getAttribute('data-speed');
        if (i === ads.length - 1) {
            ads[ads.length - 1].classList.remove('rotator__case_active');
            ads[0].classList.add('rotator__case_active');
        }
        if (ads[i].classList.contains('rotator__case_active')) {
            ads[i].classList.remove('rotator__case_active');
            ads[i+1].classList.add('rotator__case_active');
            break;
        }
    }
}

setInterval(rotate, 1000)