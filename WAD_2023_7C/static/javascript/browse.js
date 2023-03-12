const prev = document.querySelector("#prev")
const next = document.querySelector("#next")

let i = 0
let recipes = document.querySelectorAll(".recipe-item")

next.addEventListener("click", () => change(1));
prev.addEventListener("click", () => change(-1));

function change(change){
    let animationTime = 300;

    const animationFadeOut = [
        {
            transform:"scaleX(1)",
        },
        {
            transform:"scaleX(0)",
        }
    ];
    const animationFadeIn = [
        {
            transform:"scaleX(0)",
        },
        {
            transform:"scaleX(1)",
        }
    ];
    const control = {
        duration:animationTime,
        fill:'forwards',
    }

    if(change > 0){
        recipes[i].style.transformOrigin = "left"
    } else {
        recipes[i].style.transformOrigin = "right"
    }
    
    recipes[i].classList.remove('active')
    recipes[i].classList.add('inactive')
    recipes[i].animate(animationFadeOut,control)
    
    
    i = (i+change+recipes.length) % recipes.length

    recipes[i].classList.add('active')
    recipes[i].classList.remove('inactive')

    if(change <= 0){
        recipes[i].style.transformOrigin = "left"
    } else {
        recipes[i].style.transformOrigin = "right"
    }

    recipes[i].animate(animationFadeIn, control)
}