
$(window).scroll(function()
{
    if($(window).scrollTop() >= ($(document).height() - $(window).height()) - 10)
    {
        var destination = "../ajax/" + $('#postsWrapper').children().length;

        $.ajax(
            {
                type: 'POST',
                url: destination,
                data: JSON.stringify({comment: 'Hello'}),
                dataType: 'text',
                contentType: 'application/json; charset=utf-8',
                success: function (response)
                {
                    var wrapper = $('#postsWrapper')
                    wrapper.append(response)
                    var post = wrapper.children().last()

                    $('.tooltip', post).css('display', 'none')

                    $('.tooltip', post).prev().mouseover(function(){
                        $(this).next().css('display' , 'block');
                    });

                    $('.tooltip', post).prev().mouseout(function(){
                        $(this).next().css('display' , 'none');
                    });

                    addComment($('.post_incm form', post))
                    likePost($('.likeLink', post))
                    $('.likeCommentDiv span', post).addClass('like-comment')
                }
            })
    }
});


function addComment(form)
{
    form.on("submit" , function(e)
    {
        e.preventDefault()

        var destination = $(this).attr('action')
        var commentBody = $('textarea', this).val()
        var cm_wrapper = $(this).parent()

        $.ajax(
            {
                type: 'POST',
                url: destination,
                data: JSON.stringify({comment: commentBody}),
                dataType: 'text',
                contentType: 'application/json; charset=utf-8',
                success: function (response)
                {
                    cm_wrapper.prev().prepend(response)
                    $('textarea', cm_wrapper).val('')
                }
            })
    });
}


function likePost(likeLink)
{
    likeLink.on('click', function(e)
    {
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
}