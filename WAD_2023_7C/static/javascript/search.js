const searchBar = document.querySelector('#searchbar > input')
if(searchBar != null) searchBar.addEventListener("input", () => {
    let query = searchBar.value.toLowerCase()
    search(query)
})

function search(query){
    const recipes = document.querySelectorAll(".grid-item");
    for(i = 0; i < recipes.length; i++){
        recipes[i].style.display = "block";
    }
    if(query == undefined) return;
    for(i = 0; i < recipes.length; i++){
        let recipeText = recipes[i].querySelector('span').innerHTML
        recipeText = recipeText.toLowerCase()
        if(recipeText == null) continue;
        else if(!recipeText.includes(query)) {
            recipes[i].style.display = "None";
        }
    }
}