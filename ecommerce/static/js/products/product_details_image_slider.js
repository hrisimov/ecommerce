let featured = document.getElementById('featured')
let active = document.querySelector('.active')
let thumbnails = document.getElementsByClassName('thumbnail')

for (const thumbnail of thumbnails) {
    thumbnail.addEventListener('mouseover', (e) => {
        active.classList.remove('active')
        e.target.classList.add('active')
        featured.src = e.target.src
        active = e.target
    })
}

let [chevronUp, chevronDown] = document.getElementsByClassName('chevron')
let thumbnailsWrapper = document.querySelector('.thumbnails-wrapper')

chevronUp.addEventListener('click', () => {
    thumbnailsWrapper.scrollTop -= 108
})

chevronDown.addEventListener('click', () => {
    thumbnailsWrapper.scrollTop += 108
})