// Script for filling orders' progress bars

function orderProgress(orderr_dict, orderrnum_dict) {
// Script for progress bar layout

// Modified from https://www.markuptag.com/jquery-animated-progress-bar-with-percentage-counter/
    var $this = $(this);
	
    var orderr = this.parentElement.previousElementSibling.textContent
	
	var percent = 0
	var numtext = 0
	if (orderr in orderr_dict) {
		var percent = 100 * orderr_dict[orderr] / orderrnum_dict[orderr];
		var numtext = orderr_dict[orderr];
	}
	
    //$this.attr('percent', numtext);
    $this.css("width",percent+'%');
    $({animatedValue: 0}).animate({animatedValue: numtext},{
        duration: 2000,
        step: function(){
            $this.attr('percent', numtext + "/" + orderrnum_dict[orderr]);
        },
        complete: function(){
            $this.attr('percent', numtext + "/" + orderrnum_dict[orderr]);
        }
		
    });
}
