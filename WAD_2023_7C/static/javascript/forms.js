const options = {
    'cooking': ["Chinese", "Greek", "Indian", "Italian", "Mexican", "Thai"],
    'baking': ["Bread", "Brownies", "Cookies", "Cake", "Cupcake", "Pastries"],
}  

const categorySelect = document.querySelector("#categorySelect");
const cuisineSelect = document.querySelector("#cuisineSelect");

addOptions('cooking')

categorySelect.addEventListener("change", () => {
    addOptions(categorySelect.value);
})  
 
function addOptions(category){
    cuisineSelect.innerHTML = "";
    let formOptions = options[category];
    for(i = 0; i < formOptions.length; i++){
        cuisineSelect.innerHTML += `<option value="${formOptions[i].toLowerCase()}">${formOptions[i]}</option>`
    }
}