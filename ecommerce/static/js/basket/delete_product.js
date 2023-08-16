let deleteButtons = document.getElementsByClassName('delete');

for (const button of deleteButtons) {
    button.addEventListener('click', deleteProduct);
}

async function deleteProduct() {
    let article = this.parentElement.parentElement;
    let productId = article.id;

    try {
        let response = await fetch(deleteURL, {
            method: "POST",
            headers: {
                'content-type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({productId}),
        });
        updateTemplate(article, await response.json());
    } catch (error) {
        console.log(error);
    }
}

function updateTemplate(article, {basketTotalQuantity, subtotalPrice}) {
    article.remove();
    document.querySelector('.header .products-count').textContent = basketTotalQuantity;
    document.querySelector('.main .wrapper > div .value').textContent = `${subtotalPrice}$`;

    if (basketTotalQuantity === 0) {
        let h2 = document.createElement('h2');
        h2.classList.add('subtitle');
        h2.textContent = 'Your basket is empty.';
        document.querySelector('.main .basket').appendChild(h2);
        document.querySelector('.main .wrapper > div').remove();
    }
}
