$(document).ready(function() {
    feather.replace();
    let liked = false;
    let username
    username = $('#like-button').attr('data-username');
    if(username == undefined) return;
    let recipe_name
    recipe_name = $('#like-button').attr('data-recipename');

    $.get('/yumyay/has_user_liked_recipe/', 
    {'name': recipe_name, 'user': username}, 
    function(data) {
        if(data === '1'){
            $('#like-button').removeClass('unliked')
            $('#like-button').addClass('liked')
            liked = true;
        }
    });

    $('#like-button').click(function() {
        passLike = ""
        if(!liked){
            passLike = 'like'
        } else {
            passLike = 'dislike'
        }   
        
        $.get('/yumyay/like_recipe/', 
            {'name': recipe_name, 'user': username, 'like': passLike}, 
            function(data) {
                $('.like-info').html(data + " likes")
                $('#like-button').toggleClass('unliked')
                $('#like-button').toggleClass('liked')
        });
        liked = !liked;
    });
})