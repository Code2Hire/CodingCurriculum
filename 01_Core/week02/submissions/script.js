//DOM ELEMENTS
saveButton = document.querySelector(".contact-form-button");
saveButton.addEventListener("click", generateNameList());

function Person(firstName, lastName){
    this.firstName = firstName;
    this.lastName = lastName;
}

function generateNameList(e){
    e.preventDefault();

    const test = document.querySelectorAll("input").value;

    console.log(test);
}
