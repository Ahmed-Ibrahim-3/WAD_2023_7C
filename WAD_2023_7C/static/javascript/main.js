// Main JavaScript file
console.log('Main loaded')

// Buttons Cooking/Baking
const cbButton = document.querySelectorAll(".btn-rounded");

cbButton.forEach(cButton => {
    cButton.addEventListener("click", () => {
        var scaleFactor = 0.8;
        var transitionDuration = "0.1s";

        cButton.style.transform = `scale(${scaleFactor})`;
        cButton.style.transition = `transform ${transitionDuration}`;
        setTimeout(() => {
            cButton.style.transform = "";
            cButton.style.transition = "";
          }, 110);
    })
})

// Home Page Buttons
const lrButtons = document.querySelectorAll(".side-btn");

lrButtons.forEach(sButton => {
    sButton.addEventListener("click", () => {
        var scaleFactor = 0.8;
        var transitionDuration = "0.1s";

        sButton.style.transform = `scale(${scaleFactor})`;
        sButton.style.transition = `transform ${transitionDuration}`;
        setTimeout(() => {
            sButton.style.transform = "";
            sButton.style.transition = "";
          }, 90);
    })
})