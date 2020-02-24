
/* Makes selecting favorite sport blank by default */
document.getElementById("sportoptions").selectedIndex = -1;




// I DON'T FULLY UNDERSTAND WHAT'S GOING ON FROM HERE DOWN. Have been working for hours on trying to get the last 'Very Hard' portion of the Toy Problems and I can't figure it out. This code is pretty much all from the example that was in the submissions folder. Need help/explanation of what's going on so I can fully grasp the concept and not just have the code work without my understanding. 

 // create an alphabetically-sorted list by last name.
 function getNames(){
  var names = document.getElementById("myText").value; //points to the value of the textArea.
  var namesArr = names.split(',');   //Splits the names with a comma 
  var sortedNames = namesArr.sort(); //sorts the names in acending order
  var fullHTML = sortedNames.join(' ') // joins  the names with a space
  document.getElementById("list").innerHTML = fullHTML;   //replaces the content in the empty div with the new array of names.
}

// string of full names

var names = ["Nick Koehne", "Kelton Williams", "Sam Childress", "Pat Ellison"];

var allNames = names.sort((a,b) => {  //Compare function that takes in the name and last name and compares them.
  var aSplit = a.split(' ');        // splits the first parameter with a space    
  var aLastName = aSplit[1].toLowerCase();   // looks at the second value of the a parameter (the last name)
  var bSplit = b.split(' ');                  // splits the second parameter ('Kelton Williams')
  var bLastName = bSplit[1].toLowerCase();  // looks at the second value of the parameter ('williams')
  if(aLastName < bLastName) return -1;    // if the first last name is less than the second last name puts it first.
  if(aLastName > bLastName) return 1;  // if the first last name is greater than it will put it after .
  return 0;
})


var id = document.getElementById("list");
allNames.forEach((i)=>{
  var newDiv = document.createElement('li');   // creater an new list that takes all the names
  id.appendChild(newDiv)  //adds the list to the empty names div
  newDiv.classList.add("addCSS");
  newDiv.innerHTML = i;  // prints the names by replacing the text in the empty div.
})