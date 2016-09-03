

$('header .header_input').on('keyup', function(e)
{
    e.preventDefault()

    var input = $(this)
    var type = input.prev().val()
    var searchText = input.val()
    var destination = input.parent().attr('action')

    $('#movieResult').html('')
    $('#usersResult').html('')

    $.ajax(
            {
                type: 'GET',
                dataType: 'text',
                url: destination + '?search=' + searchText + '&type=1&isInSearch=true',
                contentType: 'application/json; charset=utf-8',
                success: function (response)
                {
                        console.log(response)
                        $('#movieResult').append(response);
                }
            })

    $.ajax(
            {
                type: 'GET',
                dataType: 'text',
                url: destination + '?search=' + searchText + '&type=2&isInSearch=true',
                contentType: 'application/json; charset=utf-8',
                success: function (response)
                {
                        console.log(response)
                        $('#usersResult').append(response);
                        follow_unfollow($('#usersResult .ff_button'))
                }
            })
});



function follow_unfollow(ff_button)
{
    ff_button.on('click', function(e)
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
}