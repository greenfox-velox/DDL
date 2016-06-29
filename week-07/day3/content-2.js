// fill every paragraph with the last one's content.
//

var paragraphs = document.querySelectorAll('p');
var new_paragraphs = document.querySelector('.dog');

paragraphs.forEach(function (e) {
    e.textContent = new_paragraphs.textContent
});
