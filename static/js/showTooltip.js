$('.tooltip').css('display' , 'none');

$('.tooltip').prev().mouseover(function(){
    $(this).next().css('display' , 'block');
});

$('.tooltip').prev().mouseout(function(){
    $(this).next().css('display' , 'none');
});