

$('.likeLink').on('click', function(e){
    e.preventDefault();
    var destination = $(this).attr('href')
    var spanNumLikes = $(this).next()

    $.ajax(
        {
            type: 'POST',
            url: destination,
            data: '',
            dataType: 'text',
            contentType: 'application/json; charset=utf-8',
            success: function (response)
            {
                console.log(response)
                if(response == 'Post successfully Liked !')
                {
                    spanNumLikes.html(parseInt(spanNumLikes.html())+1)
                    spanNumLikes.addClass('likedPost')
                }

                else
                {
                    spanNumLikes.html(parseInt(spanNumLikes.html())-1)
                    spanNumLikes.removeClass('likedPost')
                }
            }
        })
});