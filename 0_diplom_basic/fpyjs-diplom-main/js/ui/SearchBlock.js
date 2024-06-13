/**
 * Класс SearchBlock
 * Используется для взаимодействием со строкой ввода и поиска изображений
 * */
class SearchBlock {
  constructor( element ) {
    this.element = element;
    this.registerEvents();
  }

  /**
   * Выполняет подписку на кнопки "Заменить" и "Добавить"
   * Клик по кнопкам выполняет запрос на получение изображений и отрисовывает их,
   * только клик по кнопке "Заменить" перед отрисовкой очищает все отрисованные ранее изображения
   */
  registerEvents(){
    document.querySelector('.search-block').addEventListener('click', (e) => {
      const replace = document.querySelector('.replace');
      const add = document.querySelector('.add');
      const input = document.querySelector('input');
      if (e.target == replace || e.target == add) {
        if (input.value.trim() != '') {
          if (e.target == replace) {
            App.imageViewer.clear();
          } else {
            try {
              VK.get(input.value, App.imageViewer.drawImages);
            }
            catch (e) {
              alert('Ошибка' + e.name + ':' + e.message);
            }
          };
        };
      };
    });
  }
}