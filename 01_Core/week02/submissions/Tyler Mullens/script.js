// not realy sure how to get this to work. Seems to put things out of order when they are entered and does not apply css to additions
function nameFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {  
    var myDropdown = document.getElementById("myDropdown");
      if (myDropdown.classList.contains('show')) {
        myDropdown.classList.remove('show');
      }
    }
  }
function getNames(){
    var names = document.getElementById("myText").value;
    var namesArr = names.split(',');
    var sortedNames = namesArr.sort(); 
    var fullHTML = sortedNames.join(' ')
    document.getElementById("list").innerHTML = fullHTML; 
}

var names = ["Tyler Mullens", "Jessica Pelfrey", "Brennen Jonatzke", "Nick Koehne"];

var allNames = names.sort((a,b) => {
 var aSplit = a.split(' '); 
 var aLastName = aSplit[1].toLowerCase(); 
 var bSplit = b.split(' '); 
 var bLastName = bSplit[1].toLowerCase();
 if(aLastName < bLastName) return -1; 
 if(aLastName > bLastName) return 1; 
 return 0;
})


var id = document.getElementById("list");
allNames.forEach((i)=>{
  var newDiv = document.createElement('li'); 
  id.appendChild(newDiv) 
  newDiv.classList.add("add");
  newDiv.innerHTML = i; 
})

