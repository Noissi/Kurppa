// Script for percentage circle
function animateCircle(percentage) {
    var number = 100 - percentage;

	document.documentElement.style.setProperty('--my-percentage', percentage);
	document.documentElement.style.setProperty('--my-percentage-left', number);
	document.getElementById('circle').setAttribute("stroke-dasharray", percentage + " " + number);
};
