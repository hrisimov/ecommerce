let updateButtons = document.getElementsByClassName('update');

for (const button of updateButtons) {
    button.addEventListener('click', updateProduct);
}

async function updateProduct() {
    let article = this.parentElement.parentElement;
    let productId = article.id;
    let select = this.previousElementSibling.querySelector('select');
    let quantity = select.value;

    try {
        let response = await fetch(updateURL, {
            method: "POST",
            headers: {
                'content-type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({productId, quantity}),
        });
        applyUpdatedValues(select, await response.json());
    } catch (error) {
        console.log(error);
    }
}

function applyUpdatedValues(select, {productQuantity, productStock, basketTotalQuantity, subtotalPrice}) {
    let selectMaxQuantity = Math.min(productQuantity + 10, productStock);
    select.innerHTML = '';

    for (let q = 1; q <= selectMaxQuantity; q++) {
        let option = document.createElement('option');
        option.value = q;
        option.text = q;
        if (q === productQuantity) {
            option.selected = true;
        }
        select.appendChild(option);
    }

    document.querySelector('.header .products-count').textContent = basketTotalQuantity;
    document.querySelector('.main .wrapper > div .value').textContent = `${subtotalPrice}$`;
}
