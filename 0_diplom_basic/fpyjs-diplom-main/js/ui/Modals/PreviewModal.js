/**
 * Класс PreviewModal
 * Используется как обозреватель загруженный файлов в облако
 */
class PreviewModal extends BaseModal {
  constructor(element) {
    super(element);
    this.element = document.querySelector('.uploaded-previewer-modal');
    this.content = this.element.querySelector('.content');
    this.registerEvents();
  }

  /**
   * Добавляет следующие обработчики событий:
   * 1. Клик по крестику на всплывающем окне, закрывает его
   * 2. Клик по контроллерам изображения: 
   * Отправляет запрос на удаление изображения, если клик был на кнопке delete
   * Скачивает изображение, если клик был на кнопке download
   */
  registerEvents() {
    this.element.addEventListener('click', (e) => {
      if (e.target.classList.contains('x')) {
        this.close();
      }
    })

    this.content.addEventListener('click', (e) => {
      if (e.target.classList.contains('delete')) {
        e.target.querySelector('i').className = 'icon spinner loading';
        e.target.classList.add('disabled');
        const path = e.target.dataset.version != 'undefined'? `${e.target.dataset.path} ${e.target.dataset.version}`: e.target.dataset.path;
        Yandex.removeFile(path, (resp) => {
          if (typeof(resp) === 'object') {
            e.target.closest('.image-preview-container').remove();
          }
        });
      }

      if (e.target.classList.contains('download')) {
        Yandex.downloadFileByUrl(e.target.dataset.file);
      }
    })
  }


  /**
   * Отрисовывает изображения в блоке всплывающего окна
   */
  showImages(data) {
    let dataRevers = data['items'].reverse().filter(el => el['media_type'] == 'image');
    let imagesList = [];
    dataRevers.forEach(el => imagesList.push(this.getImageInfo(el)));
    this.content.innerHTML = imagesList.join('');
  }
  /**
   * Форматирует дату в формате 2021-12-30T20:40:02+00:00(строка)
   * в формат «30 декабря 2021 г. в 23:40» (учитывая временной пояс)
   * */
  formatDate(date) {
    const newDate = new Date(date);
    let day = newDate.getDate();
    let month = new Intl.DateTimeFormat("ru-RU", {month: 'long'}).format(newDate.getMonth()).toLowerCase();
    let year = newDate.getFullYear();
    let hours = newDate.getHours();
    let minutes = newDate.getMinutes();

    return `${day} ${month} ${year} г. в ${hours}:${minutes}`;
  }

  /**
   * Возвращает разметку из изображения, таблицы с описанием данных изображения и кнопок контроллеров (удаления и скачивания)
   */
  getImageInfo(item) {
    let version = item['path'].match(/\(.+\)/gm)? item['path'].match(/\(.+\)/gm)[0]: undefined;
    return `
      <div class="image-preview-container">
        <img src=${item['preview']} />
        <table class="ui celled table">
        <thead>
          <tr><th>Имя</th><th>Создано</th><th>Размер</th></tr>
        </thead>
        <tbody>
          <tr><td>${item['name']}</td><td>${this.formatDate(item['created'])}</td><td>${item['size']} Кб</td></tr>
        </tbody>
        </table>
        <div class="buttons-wrapper">
          <button class="ui labeled icon red basic button delete" data-path=${item['path']} data-version=${version}>
            Удалить
            <i class="trash icon"></i>
          </button>
          <button class="ui labeled icon violet basic button download" data-file=${item['file']}>
            Скачать
            <i class="download icon"></i>
          </button>
        </div>
      </div>
    `
  }
}