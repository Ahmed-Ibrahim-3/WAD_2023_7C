$(document).ready(function() {
    let liked = false;

    let username
    username = $(this).attr('data-username');
    if(username == undefined) return;

    let recipe_name
    recipe_name = $(this).attr('data-recipename');

    $.get('/yumyay/has_user_liked_recipe/', 
    {'name': recipe_name, 'user': username}, 
    function(data) {
        if(data){
            $('#like-button').removeClass('unliked')
            $('#like-button').addClass('liked')
            liked = true;
        }
    });

    $('#like-button').click(function() {
        if(!liked){
            $.get('/yumyay/like_recipe/', 
            {'name': recipe_name, 'user': username}, 
            function(data) {
                $('.like-info').html(data)
                $('#like-button').removeClass('unliked')
                $('#like-button').addClass('liked')
            });
        } else {
            $.get('/yumyay/unlike_recipe/', 
            {'name': recipe_name, 'user': username}, 
            function(data) {
                $('.like-info').html(data)
                $('#like-button').removeClass('liked')
                $('#like-button').addClass('unliked')
            });
        }
        liked = !liked;
    });
})