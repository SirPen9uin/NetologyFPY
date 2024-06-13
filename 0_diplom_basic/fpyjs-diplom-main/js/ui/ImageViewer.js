/**
 * Класс ImageViewer
 * Используется для взаимодействием блоком изображений
 * */
class ImageViewer {
  constructor( element ) {
    this.element = element;
    this.fluidImage = document.querySelector('.fluid');
    this.registerEvents();
  }

  /**
   * Добавляет следующие обработчики событий:
   * 1. Клик по изображению меняет класс активности у изображения
   * 2. Двойной клик по изображению отображает изображаения в блоке предпросмотра
   * 3. Клик по кнопке выделения всех изображений проверяет у всех ли изображений есть класс активности?
   * Добавляет или удаляет класс активности у всех изображений
   * 4. Клик по кнопке "Посмотреть загруженные файлы" открывает всплывающее окно просмотра загруженных файлов
   * 5. Клик по кнопке "Отправить на диск" открывает всплывающее окно для загрузки файлов
   */
  registerEvents(){
    const body = document.querySelector('body');
    body.addEventListener('dblclick', (e) => {
      if (e.target.closest('.four')) {
        this.fluidImage.setAttribute('src', `${e.target.getAttribute('src')}`);
      }
    });

    body.addEventListener('click', (e) => {
      if (e.target.closest('.four')) {
        e.target.classList.toggle('selected');
        this.checkButtonText();
      };

      if (e.target.classList.contains('select-all')) {
        const images = [...document.querySelectorAll('.four')];
        const imagesActive = images.filter(el => el.querySelector('img').classList.contains('selected'));
        if (imagesActive.length == images.length) {
          images.forEach(el => el.querySelector('img').classList.remove('selected'));
        } else {
          images.forEach(el => el.querySelector('img').classList.add('selected'));
        };
        this.checkButtonText();
      }

      if (e.target.classList.contains('show-uploaded-files')) {
        let filePreviewer = App.getModal('filePreviewer');
        filePreviewer.open();
        let funcImagesBind = filePreviewer.showImages.bind(filePreviewer);
        Yandex.getUploadedFiles(funcImagesBind);
        
      }

      if (e.target.classList.contains('send')) {
        let fileUploader = App.getModal('fileUploader');
        let imagesActive = [...document.querySelectorAll('.four')].filter(el => el.querySelector('img').classList.contains('selected'));
        fileUploader.open();
        fileUploader.showImages(imagesActive);
        imagesActive.forEach(el => el.querySelector('img').classList.remove('selected'));
      }

    });
  }

  /**
   * Очищает отрисованные изображения
   */
  clear() {
    [...document.querySelectorAll('.four')].forEach(el => el.remove());
  }

  /**
   * Отрисовывает изображения.
  */
  drawImages(images) {
    const imagesWrapper = document.querySelector('.images-wrapper');
    if (images.length > 0) {
      document.querySelector('.select-all').classList.remove('disabled');
    } else {
      document.querySelector('.select-all').classList.add('disabled'); 
    };
    images.forEach(el => {
      imagesWrapper.querySelector('.row').innerHTML += `
      <div class='four wide column ui medium image-wrapper'><img src=${el} /></div>
      `
    }); 
  }

  /**
   * Контроллирует кнопки выделения всех изображений и отправки изображений на диск
   */
  checkButtonText(){
    const images = [...document.querySelectorAll('.four')];
    const imagesActive = images.filter(el => el.querySelector('img').classList.contains('selected'));
    const selectAll = document.querySelector('.select-all');
    const send = document.querySelector('.send');
    if (imagesActive.length == images.length) {
      selectAll.textContent = 'Снять выделение';
    } else {
      selectAll.textContent = 'Выбрать все';
    };

    if (imagesActive.length > 0) {
      send.classList.remove('disabled');
    } else {
      send.classList.add('disabled');
    };
  }
}