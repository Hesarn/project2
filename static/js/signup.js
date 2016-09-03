var inputBoxes = document.querySelectorAll('.login > form > div > input');

function validateEmail(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
}

function check(ind)
{
    var tmp=inputBoxes[ind].parentElement.lastChild;
    
    if(inputBoxes[ind].value.length===0)
    {
        tmp.innerText='This field is empty';
        return false;
    }
    
    if(inputBoxes[ind].value.length>0 && (ind===0 || ind===1))
        return true;
    
    if(ind == 2)
    {
        tmp.innerText = 'Email is not valid';
        var email = inputBoxes[2].value;
        if(!validateEmail(email))
            return false;
        return true;
    }
    
    if(ind == 3)
    {
        tmp.innerText = "Your password should at least have 6 letters";
        if(inputBoxes[ind].value.length<6)
            return false;
        return true;
    }
    
    if(ind==4)
    {
        tmp.innerText="Entered password doesn't match";
        if(inputBoxes[3].value!==inputBoxes[4].value)
            return false;
        return true;
    }
    
    
}

function addEventListenerTo(index)
{
    var warning = document.createElement('p');
    warning.style.fontSize = "12px";
    warning.style.color = "red";
    warning.style.display = 'none';

    inputBoxes[index].parentElement.appendChild(warning);

//    inputBoxes[index].addEventListener('blur', function () {
//    if (!check(index)) 
//    {
//        inputBoxes[index].parentElement.lastChild.style.display = 'block';
//        inputBoxes[index].style.border = "1px solid red";
//    } 
//
//    else
//    {
//        inputBoxes[index].parentElement.lastChild.style.display = 'none';
//        inputBoxes[index].style.border = 'none';
//    }}, false);
    
    document.querySelector('.login_button').addEventListener('click', function (e) {
        if (!check(index)) 
        {
            inputBoxes[index].parentElement.lastChild.style.display = 'block';
            inputBoxes[index].style.border = "1px solid red";
        } 

        else
        {
            inputBoxes[index].parentElement.lastChild.style.display = 'none';
            inputBoxes[index].style.border = 'none';
        }
        e.preventDefault();
    });
}

function birthdayValidation(ind)
{
    var tmp = document.querySelectorAll('.login div select');
    var newElement;
    
    if(ind==0)
    {
        newElement = document.createElement('p');

        newElement.innerText = 'Please enter your birthday';
        newElement.style.color = 'red';
        newElement.style.fontSize = "12px";
        newElement.style.display='none';

        tmp[ind].parentElement.appendChild(newElement);
    }
    
    else
        newElement = tmp[ind].parentElement.lastElementChild; 
        
//    tmp[ind].addEventListener('blur' , function () {
//        if(!tmp[0].value || !tmp[1].value || !tmp[2].value)
//            newElement.style.display = 'block';
//        
//        else
//            newElement.style.display = 'none';
//
//        for(var i=0 ; i<3 ; i++)
//        {
//            if(!tmp[i].value)
//                tmp[i].style.border = '1px solid red';
//
//            else
//                tmp[i].style.border = 'none';
//        }
//    });
    
    if(ind==0)
    {
        document.querySelector('.login_button').addEventListener('click' , function (e) {

//            console.log('hiiii');
            if(!tmp[0].value || !tmp[1].value || !tmp[2].value)
                newElement.style.display = 'block';

            else
                newElement.style.display = 'none';

            for(var i=0 ; i<3 ; i++)
            {
                if(!tmp[i].value)
                    tmp[i].style.border = '1px solid red';

                else
                    tmp[i].style.border = 'none';
            }
            e.preventDefault();
        });
    }

}

for(var i=0 ; i<5 ; i++)
    addEventListenerTo(i);
for(var i=0 ; i<3 ; i++)
    birthdayValidation(i);
