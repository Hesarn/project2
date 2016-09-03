$('.film_score').bind('click', function(){
    $('#rating > img').attr('src' , '/static/img/0.png');
    $('#rating > img:first-child').attr('src' , '/static/img/1.png');
    $('.popup_div textarea').val('');
});

$('div#rating img').hover(function() {
    var tmp=$(this).parent().children().eq(0);
    var rate=parseInt($(this).attr('rate'));

    for(var i=1 ; i<=rate ; i++)
    {
        tmp.attr('src' , '/static/img/1.png');
        tmp=tmp.next();
    }
    
    for(var j=rate+1 ; j<=10 ; j++)
    {
        tmp.attr('src' , '/static/img/0.png');
        tmp=tmp.next();
    }
});

$('div#rating').mouseleave(function() {
    var tmp = $(this).children().eq(0);
    var rate = parseInt($(this).attr('rate'));
        
    if(rate)
    {      
        for(var i=1 ; i<=rate ; i++)
        {
            tmp.attr('src' , '/static/img/1.png');
            tmp=tmp.next();
        }

        for(var j=rate+1 ; j<=10 ; j++)
        {
            tmp.attr('src' , '/static/img/0.png');
            tmp=tmp.next();
        }
    }
    
    else
    {
        for(var i=1 ; i<=10 ; i++)
        {
            tmp.attr('src' , '/static/img/0.png');
            tmp=tmp.next();
        }
    }
});

$('div#rating img').click(function() {
    $(this).parent().attr('rate' , $(this).attr('rate'));
});