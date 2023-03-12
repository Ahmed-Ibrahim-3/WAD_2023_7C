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

