window.onload = function () {
  var canvas = document.getElementById("canvas"),
      context = canvas.getContext("2d"),
      width = canvas.width = window.innerWidth,
      height = canvas.height = window.innerHeight;
  
  // Resize the canvas y axis so that the sin wave fits in
  context.translate(0, height / 2);
  // Reverse y axis in canvas to show the expected sin wave shape
  context.scale(1, -1);
  
  for(var angle = 0; angle < Math.PI * 2; angle += 0.01) {
    var x = angle * 200,
        y = Math.sin(angle) * 200;
    
    context.fillRect(x, y, 5, 5);
  }
}