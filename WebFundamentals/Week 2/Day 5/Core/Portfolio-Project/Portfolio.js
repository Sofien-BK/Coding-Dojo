function changeLink() {
    window.location.href = "https://github.com/Sofien-BK"
}
var i = 0;
var txt = 'Hello, I"m the student developer destined for greatness'; /* The text */
var speed = 50; /* The speed/duration of the effect in milliseconds */


var h1Text = document.getElementById("bio").textContent;
        var container = document.getElementById("bio");
        container.textContent = "";
        for (var i = 0; i < h1Text.length; i++) {
    setTimeout(function (i) {
        return function () {
        container.textContent += h1Text[i];
        };
      }(i), i * 350); 
    }