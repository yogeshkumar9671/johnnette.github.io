const box = document.querySelectorAll('.box_container');

const boxObserver = new IntersectionObserver((entries) => {
    const ON_SCRENN = 'on_screen'
    entries.forEach(entry => {
        const { isIntersecting, target } = entry

        if (isIntersecting) {
            target.classList.add(ON_SCRENN)
            return true
        }
        target.classList.remove(ON_SCRENN)
    })
}, {
    threshold: 0.5,
})


box.forEach((box) => {
    boxObserver.observe(box)
})