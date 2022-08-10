// Replace placeholder images with the corresponding bird image
function getBirdImage(birds) {

    var $this = $(this);
    var birdname = this.nextElementSibling.firstElementChild.innerText;
    
	for (let i = 0; i < birds.length; i++) {
		var name = birds[i][3];
		if (birdname == name) {
		    var img_url = birds[i][8];
		    if (img_url != null) {
		    	$(this.firstElementChild).attr('src', img_url);
		    }
		    break;
		}
	}
}
