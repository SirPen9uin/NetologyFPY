const bar = document.getElementById('progress');
const form = document.getElementById('form');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const xhr = new XMLHttpRequest();
    xhr.upload.onprogress = function(e) {
        bar.setAttribute('max', e.total);
        bar.value = e.loaded;
    }
    xhr.open('POST', 'https://students.netoservices.ru/nestjs-backend/upload');
    const formData = new FormData(form);
    xhr.send(formData);
})