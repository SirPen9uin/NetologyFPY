const products = document.querySelectorAll('.product');
const cart = document.querySelector('.cart');

products.forEach(product => {
  const id = product.getAttribute('data-id');
  const quantityControls = product.querySelector('.product__quantity-controls');
  const quantityValue = quantityControls.querySelector('.product__quantity-value');

  quantityControls.addEventListener('click', event => {
    const target = event.target;
    if (target.classList.contains('product__quantity-control_dec')) {
      if (quantityValue.textContent > 1) {
        quantityValue.textContent--;
      }
    } else if (target.classList.contains('product__quantity-control_inc')) {
      quantityValue.textContent++;
    }
  });

  product.addEventListener('click', () => {
    let cartProduct = cart.querySelector(`[data-id="${id}"]`);
    if (!cartProduct) {
      cartProduct = document.createElement('div');
      cartProduct.classList.add('cart__product');
      cartProduct.setAttribute('data-id', id);
      cart.appendChild(cartProduct);
    }
    const image = product.querySelector('.product__image');
    const imageSrc = image.getAttribute('src');
    const cartProductImage = cartProduct.querySelector('.cart__product-image');
    if (!cartProductImage) {
      cartProductImage = document.createElement('img');
      cartProductImage.classList.add('cart__product-image');
      cartProductImage.setAttribute('src', imageSrc);
      cartProduct.appendChild(cartProductImage);
    }
    const cartProductCount = cartProduct.querySelector('.cart__product-count');
    if (!cartProductCount) {
      cartProductCount = document.createElement('div');
      cartProductCount.classList.add('cart__product-count');
      cartProduct.appendChild(cartProductCount);
    }
    cartProductCount.textContent = parseInt(cartProductCount.textContent) + parseInt(quantityValue.textContent);
  });
});