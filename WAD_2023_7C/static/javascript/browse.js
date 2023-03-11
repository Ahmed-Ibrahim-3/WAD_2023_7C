const prev = document.querySelector("#prev")
const next = document.querySelector("#next")

let i = 0
let recipes = document.querySelectorAll(".recipe-item")

next.addEventListener("click", () => change(1));
prev.addEventListener("click", () => change(-1));

function change(change){
    recipes[i].classList.remove('active')
    recipes[i].classList.add('inactive')

    i = (i+change+recipes.length) % recipes.length

    recipes[i].classList.add('active')
    recipes[i].classList.remove('inactive')
}