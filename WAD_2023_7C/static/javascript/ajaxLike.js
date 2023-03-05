$(document).ready(function() {
    // TODO -> load 'liked' from user data when showing recipe?
    let liked = false
    $('#like-button').click(function() {
        if(!liked){
            let recipe_name
            recipe_name = $(this).attr('data-recipename');

            $.get('/yumyay/like_recipe/', 
            {'name': recipe_name}, 
            function(data) {
                $('.like-info').html(data)
                $('#like-button').removeClass('unliked')
                $('#like-button').addClass('liked')
            });
        } else {
            let recipe_name
            recipe_name = $(this).attr('data-recipename');

            $.get('/yumyay/unlike_recipe/', 
            {'name': recipe_name}, 
            function(data) {
                $('.like-info').html(data)
                $('#like-button').removeClass('liked')
                $('#like-button').addClass('unliked')
            });
        }
        liked = !liked;
    });
})