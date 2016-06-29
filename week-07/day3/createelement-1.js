// Add an item that says 'The Green Fox' to the asteroid list.
// Add an item that says 'The Lamplighter' to the asteroid list.
// Add a heading saying 'I can add elements to the DOM!' to the .container.
// Add an image, any image, to the container.

var ul_list = document.querySelector('ul.asteroids')
var newLi = document.createElement('li');
newLi.id = 'b555';
newLi.textContent = 'The Green Fox';
ul_list.appendChild(newLi);

var newLi2 = document.createElement('li');
newLi2.id = 'b556';
newLi2.textContent = 'The Lamplighter';
ul_list.appendChild(newLi2);

var container = document.querySelector('.container')
var heading = document.createElement('h1');
heading.innerHTML = 'I can add elements to the DOM!';
container.appendChild(heading);

var image =  document.createElement('img');
image.src = 'kisherceg.jpg';
container.appendChild(image);
