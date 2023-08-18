let deleteButtons = document.getElementsByClassName('delete-address-link');

for (const button of deleteButtons) {
    button.addEventListener('click', deleteAddress);
}

async function deleteAddress() {
    let article = this.parentElement.parentElement;
    let addressId = article.id;

    try {
        let response = await fetch(deleteURL, {
            method: "POST",
            headers: {
                'content-type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({addressId}),
        });
        await response.json();
        updateTemplate(article);
    } catch (error) {
        console.log(error);
    }
}

function updateTemplate(article) {
    article.remove();

    let hasAddresses = document.querySelector('.card') !== null;

    if (!hasAddresses) {
        let h2 = document.createElement('h2');
        h2.textContent = 'You don\'t have addresses.';
        document.querySelector('.cards').appendChild(h2);
    }
}
