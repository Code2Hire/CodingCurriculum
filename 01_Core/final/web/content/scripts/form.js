function validateName() {
    var x = document.forms["myForm"]["name"].value;
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }
}

function validateEmail() {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(document.forms["myForm"]["email"].value)) {
        return true;
    }
    console.log(document.forms["myForm"]["email"]);
    alert("You have entered an invalid email address!");
    return (false);
}

function validateNum() {
    inputnum = document.forms["myForm"]["phone"].value;
    var phonenum = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (inputnum.match(phonenum)) {
        return true;
    } else {
        alert("Invalid phone number");
        return false;
    }
}

function validateMess() {
    x = document.forms["myForm"]["message"].value;
    if (x == "") {
        alert("You forgot to leave a comment or question.");
        return false;
    }
}

function validateForm() {
    validateName();
    validateEmail();
    validateNum();
    validateMess();
}
