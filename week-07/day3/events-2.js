// On the click of the button,
// Count the items in the list
// And display the result in the result element.

var ul_list = document.querySelectorAll('ul li');
var li_counter = document.querySelector('.result');

function li_counting () {
    li_counter.textContent = ul_list.length;
}

var button = document.querySelector('button');
button.addEventListener('click', li_counting)
