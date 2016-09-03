$('#notif_pic').bind('click' , function(e){
    if($('#notif').css('display')=='none')
        $('#notif').fadeIn(200);
    else
        $('#notif').fadeOut(200);
    
    return false;
});

