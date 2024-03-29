const options = {
    'C': ["Chinese", "Greek", "Indian", "Italian", "Mexican", "Thai"],
    'B': ["Bread", "Brownies", "Cookies", "Cake", "Cupcakes", "Pastries"],
}  

const categorySelect = document.querySelector("#id_category");
const cuisineSelect = document.querySelector("#id_cuisine");

addOptions('C')

const fileButton = document.querySelector('.file-input-button')
const previewElement = document.querySelector('.image-preview')

fileButton.addEventListener('change', (e) => preview(e))

categorySelect.addEventListener("change", () => {
    addOptions(categorySelect.value);
})  
 
function preview(e){
    let file = e.target.files

    if(file.length == 0) return;
    
    let url = URL.createObjectURL(file[0])
    
    previewElement.src = url;
}

function addOptions(category){
    cuisineSelect.innerHTML = "";
    let formOptions = options[category];
    for(i = 0; i < formOptions.length; i++){
        cuisineSelect.innerHTML += `<option value="${formOptions[i].toUpperCase()}">${formOptions[i]}</option>`
    }
}

