// replace the list items' content with items from this list:
// ['apple', 'banana', 'cat', 'dog']


var list_items = document.querySelectorAll('li');
var new_list_items = ['apple', 'banana', 'cat', 'dog'];

list_items.forEach(function (e, i){
    e.textContent = new_list_items[i]
});
//
// var paragraph2 = document.querySelector('.output1');
// console.log(paragraph2);
// var paragraph3 = document.querySelector('.output2');
// console.log(paragraph3);
//
// paragraph2.textContent = paragraph.textContent;
// paragraph3.innerHTML = paragraph.innerHTML;
