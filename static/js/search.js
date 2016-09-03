

$('header .header_input').on('keyup', function(e)
{
    e.preventDefault()

    var input = $(this)
    var type = input.prev().val()
    var searchText = input.val()
    var destination = input.parent().attr('action')

    $('#searchResult').html('')

    $.ajax(
            {
                type: 'GET',
                dataType: 'text',
                url: destination + '?search=' + searchText + '&type=' + type,
                contentType: 'application/json; charset=utf-8',
                success: function (response)
                {
                        console.log(response)
                        $('#searchResult').append(response);
                }
            })
});
