// Script for uncoloring the unseen bird images
function birdImages(elements, unique_sights) {
// Script for bird list

  for (let i = 0; i < elements.length; i++) {
    var element = elements[i];
	
	var bird = element.nextElementSibling.textContent
	if (!unique_sights.includes(bird)) {
	    $(element).css("filter", "grayscale(1)");
	    var name = element.nextElementSibling;
	    $(name).css('color', 'grey');
	    $(name.nextElementSibling).css('color', 'grey');
	}
	
	if ($(element).attr("src") == "None") {
	    $(element).attr("src", "/static/images/bird_placeholder.jpg");
	}
  }	
}
