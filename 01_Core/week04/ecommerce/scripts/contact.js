//FORM VALIDATION TEST
var contactForm = document.querySelector(".contact-form");

contactForm.addEventListener("submit", formValidation);

function formValidation(e){
    e.preventDefault();
    console.log('test');
}