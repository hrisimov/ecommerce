let setDefaultButtons = document.getElementsByClassName('set-default-address-link');

for (const button of setDefaultButtons) {
    button.addEventListener('click', setNewDefaultAddress);
}

async function setNewDefaultAddress() {
    let pinIcon = document.querySelector('.card .icon');
    let article = pinIcon?.parentElement;
    let addressId = article?.id;
    let newArticle = this.parentElement.parentElement;
    let newAddressId = newArticle.id;

    try {
        let response = await fetch(setDefaultURL, {
            method: "POST",
            headers: {
                'content-type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({addressId, newAddressId}),
        });
        await response.json();
        updateTemplateValues(article, newArticle);
    } catch (error) {
        console.log(error);
    }
}

function updateTemplateValues(article, newArticle) {
    if (article) {
        article.querySelector('.icon').remove();
        let a = document.createElement('a');
        a.href = '#';
        a.classList.add('link', 'set-default-address-link');
        a.textContent = 'Set default';
        a.addEventListener('click', setNewDefaultAddress);
        article.querySelector('.buttons').prepend(a);
    }

    let i = document.createElement('i');
    i.classList.add('fa-solid', 'fa-thumbtack', 'icon');
    newArticle.prepend(i);
    newArticle.querySelector('.set-default-address-link').remove();
}
