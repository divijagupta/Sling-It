// function testForm() {
//     event.preventDefault()
//     input_url = document.forms["myForm"]["long-url"].value;
//     if (input_url == "" || input_url.length > 1000) {
//         return false;

//     }
//     var regex = /^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$/;
//     if (regex.test(input_url) == false) {
//         return false;
//     }

//     return true;

// }


// function submitForm() {
//     if (testForm()) {       
//         document.forms["myForm"].submit();
//         document.forms["myForm"].reset();       
//     } 
//     else {
//         var elementError=document.getElementById("front-val-error")
//         elementError.innerHTML = "invalid Input";
//         elementError.style.display = "block";
       
        

//     }

// }


function copy() {
    var copyText = document.getElementById("copy-url");
    var copyStatus = document.getElementById("copy-status");
    var inp = document.createElement('input');
    document.body.appendChild(inp);
    inp.value = copyText.textContent;
    inp.select();
    document.execCommand('copy', false);
    inp.remove();
    copyStatus.innerHTML = "copied";
    copyStatus.style.color = "springgreen";
}