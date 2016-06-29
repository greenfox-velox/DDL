// Write the image's url to the console.
// Replace the image with a picture of yourself.
// Make the link point to the Green Fox Academy website.
// Disable the second button.
// Replace its text with 'Don't click me!'.

var image = document.querySelector('img');
var new_image = 'http://agenda-erp.com/www/android.png';

image.src = new_image;

var link = document.querySelector('a');
var new_link = 'http://www.greenfoxacademy.com/';

link.href = new_link;

var button1 = document.querySelector('button').disabled = true;
var button2 = document.querySelector('button.this-one');

button2.textContent = "Don't Clik Me"
