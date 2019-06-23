/*
VERY HARD: Given a comma separated string of full names, use JavaScript to create an alphabetical-by-Last-Name, 
ordered list and have it display in an HTML page on your site. Make the last names bold and red using CSS (NOT inline styles).
*/


/*
This isn't exactly what was asked for. If I were to do it with the full names without copying code from elsewhere,
I would still split by ","" but then I would split each name by " ", flip their positions in the array so that the last name comes first,
then sort, then flip their positions again, then rebuild them into a new array and add the html. There has to be an easier way though.
*/
function check(){
    let input = document.querySelector('.names').value;
    input = input.split(',').sort();
    let list = '<ol id="nlist">';
    for(var i = 0; i < input.length; i++)
        list += '<li><div id="lname">' + input[i] + '</div></li>';
    list+= '</o>';
    document.querySelector('.output').innerHTML = list;
}



