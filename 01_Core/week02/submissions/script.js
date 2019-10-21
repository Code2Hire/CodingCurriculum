var generateButton = document.querySelector("button");
generateButton.addEventListener("click", generateList);

function Person(firstName, lastName){
    this.firstName = firstName;
    this.lastName = lastName;
}

function generateList(e){
    e.preventDefault();
    var nameList = [];
    var list = document.querySelector(".name-list");
    list.innerHTML = '';

    var userInput = document.querySelector(".user-input").value;
    
    nameListArr = userInput.split(", ");

    nameListArr.forEach(element => {
        const newArr = element.split(" ");
        const person = new Person(newArr[0], newArr[1]);
        nameList.push(person);
    });

    nameList.sort((a, b) => (a.lastName > b.lastName) ? 1 : -1);

    nameList.forEach(element => {
        list.innerHTML += `<li>${element.firstName} <span class="red-word">${element.lastName}</span></li>`;
    });
    
    document.querySelector(".js-fun-form").reset();
}