const searchBar = document.querySelector('#searchbar > input')
if(searchBar != null) searchBar.addEventListener("input",
    () => {
        console.log(searchBar)
        let query = searchBar.value.toLowerCase()
        console.log(query)
        search(query)
    }
)

function search(query){
    const recipes = document.querySelectorAll(".recipe-search");
    for(i = 0; i < recipes.length; i++){
        recipes[i].style.display = "none";
    }
    if(query == undefined) return;
    for(i = 0; i < recipes.length; i++){
        let recipeText = recipes[i].querySelector('span').innerHTML
        recipeText = recipeText.toLowerCase()
        if(query == "" || recipeText==null) {
                    recipes[i].style.display = "none";
        }
        else if(recipeText.includes(query)) {
            recipes[i].style.display = "block";
        }
    }
    const cuisines = document.querySelectorAll(".grid-item");
    for(i = 0; i < cuisines.length; i++){
        cuisines[i].style.display = "block";
    }
    if(query == undefined) return;
    for(i = 0; i < cuisines.length; i++){
        let cuisineText = cuisines[i].querySelector('span').innerHTML
        cuisineText = cuisineText.toLowerCase()
        if(query == "" || cuisineText==null) {
                    cuisines[i].style.display = "block";
        }
        else if(!cuisineText.includes(query)) {
            cuisines[i].style.display = "none";
        }
    }
}
