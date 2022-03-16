let menu = document.querySelector("#menu-bar");
let navbar = document.querySelector('.navbar2');
let other = document.querySelector("#other-informations")
let icons = document.querySelector('.fab-icons')

menu.onclick = () => {
    menu.classList.toggle('fa-times')
    navbar.classList.toggle('active')
    other.classList.toggle('active')
    icons.classList.toggle('active')
}

let button1 = document.querySelector('#button1')
let submenu1 = document.querySelector('#sub-menu-1')
button1.onclick = () => {
    button1.classList.toggle('fa-angle-double-up')
    submenu1.classList.toggle('active')
}
let button2 = document.querySelector('#button2')
let submenu2 = document.querySelector('#sub-menu-2')
button2.onclick = () => {
    button2.classList.toggle('fa-angle-double-up')
    submenu2.classList.toggle('active')
}
let button3 = document.querySelector('#button3')
let submenu3 = document.querySelector('#sub-menu-3')
button3.onclick = () => {
    button3.classList.toggle('fa-angle-double-up')
    submenu3.classList.toggle('active')
}