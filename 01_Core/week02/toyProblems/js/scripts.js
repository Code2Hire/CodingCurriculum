function alphaClick() {
  event.preventDefault()

  const userInput = document.getElementById("nameList").value
  const TARGET_UL_ELEMENT = document.getElementById("sortedNameList")
  let splitNames

  splitNames = userInput.split(",")
  splitNames = splitNames.map(currentElement => currentElement.trim())

  let sortedNames = flipNames(splitNames)
  sortedNames.sort()
  sortedNames = flipNames(sortedNames)

  console.log(userInput)
  console.log(splitNames)
  console.log(sortedNames)

  TARGET_UL_ELEMENT.innerHTML = ""

  sortedNames.forEach(currentName => {
    const newListItem = document.createElement("li")
    newListItem.innerText = currentName

    TARGET_UL_ELEMENT.insertAdjacentElement("beforeend", newListItem)
  })
}

const flipNames = function(nameArray) {
  let flippedNameArray = nameArray.map(function(currentName) {
    separatedName = currentName.split(" ")
    return `${separatedName[1]} ${separatedName[0]}`
  })
  return flippedNameArray
}
