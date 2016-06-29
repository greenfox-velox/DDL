// Remove the king from the list.
// Add list items that have the following text contents:
// ['apple', 'bubble', 'cat', 'green fox']


var ul_list = document.querySelector('ul.asteroids');
var the_king = document.querySelector('li');
ul_list.removeChild(the_king);

var list_of_new_text_contents = ['apple', 'bubble', 'cat', 'green fox'];
list_of_new_text_contents.forEach(function (e) {
    var newLi = document.createElement('li');
    newLi.textContent = e;
    ul_list.appendChild(newLi);
});
