const prev = document.querySelector("#prev")
const next = document.querySelector("#next")

let i = 0
let recipes = document.querySelectorAll(".recipe-item")
const amount = recipes.length

createDots(amount)

const dots = document.querySelectorAll(".dot")

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
    const animationColorOut = [
        {
            backgroundColor: '#5A8F5C',
        },
        {
            backgroundColor: 'white',
        }
    ];
    const animationColorIn = [
        {
            backgroundColor: 'white',
        },
        {
            backgroundColor: '#5A8F5C',
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
    dots[i].animate(animationColorOut, control);
    
    i = (i+change+recipes.length) % recipes.length

    recipes[i].classList.add('active')
    recipes[i].classList.remove('inactive')
    dots[i].style.backgroundColor = "black";

    if(change <= 0){
        recipes[i].style.transformOrigin = "left"
    } else {
        recipes[i].style.transformOrigin = "right"
    }

    recipes[i].animate(animationFadeIn, control)
    dots[i].animate(animationColorIn, control);
}
function createDots(amount){
    let dotContainer = document.querySelector('.map-container')
    for(let j = 0; j < amount; j++){
        let dot = document.createElement('div')
        if(j == 0) dot.style.backgroundColor = "#5A8F5C";
        dot.classList.add('dot')
        dotContainer.appendChild(dot);
    }
}