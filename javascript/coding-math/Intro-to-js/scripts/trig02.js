// Motion and animation using trig concepts

window.onload = function() {
	var canvas = document.getElementById("canvas"),
	context = canvas.getContext("2d"),
	width = canvas.width = window.innerWidth,
	height = canvas.height = window.innerHeight;

	var centerX = width * 0.5,
		centerY = height * 0.5,
		baseRadius = 100,
		baseAlpha = 0.5, //change color gradient
		offset = 50, // set to height * 0.4,
		speed = 0.05,
		angle = 0;

	// Let's call the render function
	render();

	function render() {
		var x = centerX + Math.sin(angle) * offset;
		var y = centerY + Math.sin(angle) * offset;

		var radius = baseRadius + Math.sin(angle) * offset;
		var alpha = baseAlpha + Math.sin(angle) * offset;

		context.clearRect(0,0, width, height);
		// For a fade in/out circle
		// context.fillStyle = "rgba(0,0,0, "+alpha+")";
		context.beginPath();

		// Let's move a circle along the y axis using the sine function 
		//context.arc(centerX, y, radius, 0, Math.PI * 2, false);

		// Let's move a circle along the x axis using the sine function 
		//context.arc(x, centerY, radius, 0, Math.PI * 2, false);

		// For a pulsating circle
		context.arc(centerX, centerY, radius, 0, Math.PI * 2, false);

		// Fill the circle
		context.fill();

		// Increase the angle used by the trig function
		angle += speed;

		requestAnimationFrame(render);
	}
}
