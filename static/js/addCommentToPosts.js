function addComment()
{
    $('.commentOnPost').on("submit" , function(e)
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

                    var numberOfcomments = parseInt($('.numberOfComments', cm_wrapper.parent()).html())
                    $('.numberOfComments', cm_wrapper.parent()).html(numberOfcomments+1)
                }
            })
    });
}

addComment();
