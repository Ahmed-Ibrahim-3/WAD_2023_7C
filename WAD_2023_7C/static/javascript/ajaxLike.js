$(document).ready(function() {
    feather.replace();
        

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

            $.get('/yumyay/like_recipe/', 
                {'name': recipe_name, 'user': username, 'like': passLike}, 
                function(data) {
                    $(likeInfo).html(data + " likes")
                    $(element).toggleClass('unliked')
                    $(element).toggleClass('liked')
            });
        });
    })
})