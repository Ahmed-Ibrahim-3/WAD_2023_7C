const options = {
    'C': ["Chinese", "Greek", "Indian", "Italian", "Mexican", "Thai"],
    'B': ["Bread", "Brownies", "Cookies", "Cake", "Cupcakes", "Pastries"],
}  

const categorySelect = document.querySelector("#id_category");
const cuisineSelect = document.querySelector("#id_cuisine");

addOptions('C')

categorySelect.addEventListener("change", () => {
    addOptions(categorySelect.value);
})  
 
function addOptions(category){
    cuisineSelect.innerHTML = "";
    let formOptions = options[category];
    for(i = 0; i < formOptions.length; i++){
        cuisineSelect.innerHTML += `<option value="${formOptions[i].toUpperCase()}">${formOptions[i]}</option>`
    }
}