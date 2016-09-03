function showTab()
{
    $('#userTab').bind('click' , function() {
        $('#usersResult').css('display' , 'block');
        $('#movieResult').css('display' , 'none');
        $('#userTab').css('background-color' , '#fcfcfc');
        $('#movieTab').css('background-color' , 'rgba(32, 33, 32, 0.6)');
    });
    
    $('#movieTab').bind('click' , function() {
        $('#usersResult').css('display' , 'none');
        $('#movieResult').css('display' , 'block');
        $('#userTab').css('background-color' , 'rgba(32, 33, 32, 0.6)');
        $('#movieTab').css('background-color' , '#fcfcfc');

    });
}


$('#movieResult').css('display' , 'none');
$('#userTab').css('background-color' , '#fcfcfc');
$('#movieTab').css('background-color' , 'rgba(32, 33, 32, 0.6)');
showTab();