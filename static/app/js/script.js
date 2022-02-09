let menu = document.querySelector("#menu");
let navbar = document.querySelector(".navbar");
let btn = document.querySelector(".user");

menu.onclick = () => {
    menu.classList.toggle('fa-times')
    navbar.classList.toggle('active')
    btn.classList.toggle('active')
}