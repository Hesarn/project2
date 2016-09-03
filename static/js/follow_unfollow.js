
$('.ff_button').on('click', function(e)
{
    e.preventDefault()
    destination = $(this).parent().attr('href')
    box = $(this)

    followText = $('.ezClass span', box.parent().parent().parent())

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

                if(box.hasClass('follow'))
                {
                    box.removeClass('follow')
                    box.addClass('unfollow')
                    box.attr('value', 'Unfollow')
                    followText[1].innerHTML = parseInt(followText[1].innerHTML) + 1
                }

                else
                {
                    box.addClass('follow')
                    box.removeClass('unfollow')
                    box.attr('value', 'Follow')
                    followText[1].innerHTML = parseInt(followText[1].innerHTML) - 1
                }
            }
        }
    )
})