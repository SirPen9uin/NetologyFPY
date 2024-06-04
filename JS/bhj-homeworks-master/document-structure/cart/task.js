const plus = document.getElementsByClassName('product__quantity-control product__quantity-control_inc');
const minus = document.getElementsByClassName('product__quantity-control product__quantity-control_dec');
const quantity = document.getElementsByClassName('product__quantity-value');
const add = document.getElementsByClassName('product__add');
const products = document.getElementsByClassName('product');
const images = document.getElementsByClassName('product__image');
const cart = document.querySelector('.cart__products');
let arryId = [];

for (let i = 0; i < plus.length; i++) {
  plus[i].onclick = () => {
    quantity[i].textContent = Number(quantity[i].textContent) + 1;
  };

  minus[i].onclick = () => {
    if (quantity[i].textContent > 1) {
      quantity[i].textContent = Number(quantity[i].textContent) - 1;
    }
  };

  add[i].onclick = () => {
    const productId = products[i].getAttribute('data-id');
    const productInCart = Array.from(cart.querySelectorAll('.cart__product')).find(
      (product) => product.getAttribute('data-id') === productId
    );

    if (productInCart) {
      productInCart.querySelector('.cart__product-count').textContent =
        Number(productInCart.querySelector('.cart__product-count').textContent) +
        Number(quantity[i].textContent);
    } else {
      cart.innerHTML += `
        <div class="cart__product" data-id="${productId}">
          <img class="cart__product-image" src="${images[i].getAttribute('src')}">
          <div class="cart__product-count">${quantity[i].textContent}</div>
        </div>
      `;
    }

    arryId.push(productId);
  };
}