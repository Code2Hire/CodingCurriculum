// Slideshow

var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("slides");
  if (n > x.length) {
    slideIndex = 1
  }
  if (n < 1) {
    slideIndex = x.length
  };
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex - 1].style.display = "block";
}


// Form Validation

function validateForm() {
  var name = document.forms["contactPage"]["name"].value;
  if (name == null || name == "") {
    alert("Name must be filled out.");
    return false;
  }
  var email = document.forms["contactPage"]["mail"].value;
  if (email == null || email == "") {
    alert("Email must be filled out.");
    return false;
  }
  var number = document.forms["contactPage"]["number"].value;
  if (number == null || number == "") {
    alert("Number must be filled out.");
    return false;
  }
}