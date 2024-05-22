const ads = document.querySelectorAll('.rotator__case');

function rotate() {
    for (let i = 0; i < ads.length; i++) {
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
// Повышенный уровень сложности

// function getSpeed(mass, index) {
//     return mass[index].getAttribute('data-speed');
// }

// function getIndex(mass) {
//     for (let i = 0; i < mass.length; i++) {
//         if (i === 0) {
//             return 0;
//         }
//         if (i === mass.length - 1) {
//             return 0;
//         } else {
//             return i + 1;
//         }
//     }
// }

// function rotate(mass, index) {
//     if (i === mass.length - 1) {
//         mass[index - 1].classList.remove('rotator__case_active');
//         mass[0].classList.add('rotator__case_active');
//     }
//     if (mass[index].classList.contains('rotator__case_active')) {
//         mass[index].classList.remove('rotator__case_active');
//         mass[index + 1].classList.add('rotator__case_active');
//     }
// }

// let i = getIndex(ads);
// setInterval(rotate(ads, i), getSpeed(ads, i))
setInterval(rotate, 1000)