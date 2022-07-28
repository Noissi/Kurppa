// For search method to filter birds by written text
function mySearch() {
  // Declare variables
  var input = document.getElementById('myInput');
  var filter = input.value.toUpperCase();
  
  var birdimages = document.getElementsByClassName('bird-img');

  // Loop through all list items, and hide those who don't match the search query
  for (var i = 0; birdimages[i]; i++) {
	var birdname = birdimages[i].nextElementSibling.innerText;
    if (birdname.toUpperCase().indexOf(filter) > -1) {
      birdimages[i].parentElement.style.display = "";
    } else {
      birdimages[i].parentElement.style.display = "none";
    }
  }
}
