let menu = document.querySelector("#menu-bar");
let navbar = document.querySelector('.navbar');
let icons = document.querySelector('.fab-icons');

menu.onclick = () => {
    menu.classList.toggle('fa-times')
    navbar.classList.toggle('active')
    icons.classList.toggle('active')
}
