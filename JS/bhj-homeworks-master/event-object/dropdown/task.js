let dropdown = document.querySelectorAll('.dropdown');
console.log(dropdown);
let dropdownValue = document.querySelector('.dropdown__value');
let dropdownList = document.querySelector('.dropdown__list');

dropdownValue.addEventListener('click', () => {
        dropdownList.classList.toggle('dropdown__list_active');
    });

dropdownList.addEventListener('click', (event) => {
    event.preventDefault();
    const selectedItem = event.target.textContent;
    dropdownValue.textContent = selectedItem;
    dropdownList.classList.remove('dropdown__list_active');
    });