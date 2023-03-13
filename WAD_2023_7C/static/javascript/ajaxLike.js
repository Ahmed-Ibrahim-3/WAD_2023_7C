// from https://docs.djangoproject.com/en/4.1/howto/csrf/
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    feather.replace();

    const csrftoken = getCookie('csrftoken');

    $('.like-button').each(function(){
        let element = this;   
        let username
        username = $(this).attr('data-username');
        if(username == undefined) return;
        let recipe_name
        recipe_name = $(this).attr('data-recipename');
        $.get('/yumyay/has_user_liked_recipe/', 
        {'name': recipe_name, 'user': username}, 
        function(data) {
            if(data === '1'){
                $(element).removeClass('unliked')
                $(element).addClass('liked')
            }
        });
    });
    $('.like-container').each(function(){
        let likeInfo = this.querySelector('.like-info');
        let element = this.querySelector('.like-button');
        $(element).click(function() {
            passLike = ""
            if(!this.classList.contains("liked")){
                passLike = 'like'
            } else {
                passLike = 'dislike'
            }   
            
            let username
            username = $(this).attr('data-username');
            if(username == undefined) return;
            let recipe_name
            recipe_name = $(this).attr('data-recipename');

            let data = new FormData()
            data.append('username', username)
            data.append('recipe', recipe_name)
            data.append('liked', passLike)

            const http = new XMLHttpRequest()
            http.open('POST', '/yumyay/like_recipe/')
            http.setRequestHeader('X-CSRFToken', csrftoken)
            http.onreadystatechange = function() {
                if(http.readyState == 4 && http.status == 200) {
                    $(likeInfo).html(http.responseText + " likes")
                    $(element).toggleClass('unliked')
                    $(element).toggleClass('liked')
                }
            }
            http.send(data);
        });
    })
})