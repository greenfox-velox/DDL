// Remove the king from the list.
// Add 3 list items saying 'The Fox' to the list.

var ul_list = document.querySelector('ul.asteroids');

var the_king = document.querySelector('li')
ul_list.removeChild(the_king);

var newLi = document.createElement('li')
newLi.textContent = 'The Fox';
ul_list.appendChild(newLi);

var newLi2 = document.createElement('li')
newLi2.textContent = 'The Fox';
ul_list.appendChild(newLi2);

var newLi3 = document.createElement('li')
newLi3.textContent = 'The Fox';
ul_list.appendChild(newLi3);
