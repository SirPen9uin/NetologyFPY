const plus = document.getElementsByClassName('product__quantity-control product__quantity-control_inc')
const minus = document.getElementsByClassName('product__quantity-control product__quantity-control_dec')
const quantity = document.getElementsByClassName('product__quantity-value')
const add = document.getElementsByClassName('product__add')
const products = document.getElementsByClassName('product')
const images = document.getElementsByClassName('product__image')
const cart = document.querySelector('.cart__products')
let arryId = []
for (let i = 0; i< plus.length; i++){
    plus[i].onclick = () => {
    quantity[i].textContent = Number(quantity[i].textContent)+1
    }
    minus[i].onclick = () => {
        if (quantity[i].textContent > 1){
            quantity[i].textContent = Number(quantity[i].textContent)-1
        }
    }
    add[i].onclick = () => {
        const cartCount = document.querySelectorAll('.cart__product-count')
        const productInCart = document.querySelectorAll('.cart__product')
        console.log(products[i].getAttribute('data-id'))
        
        if (arryId.includes(products[i].getAttribute('data-id') ) ) {
            cartCount[i].textContent = Number(cartCount[i].textContent) + Number(quantity[i].textContent)
        }
        else {
        cart.innerHTML +=  
       `<div class="cart__product" data-id="${products[i].getAttribute('data-id')}">
           <img class="cart__product-image" src="${images[i].getAttribute('src')}">
           <div class="cart__product-count">${quantity[i].textContent}</div>
       </div>`
        }
        arryId.push(products[i].getAttribute('data-id'))
    }
}