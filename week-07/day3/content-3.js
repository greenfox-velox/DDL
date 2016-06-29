// fill output1 with the first paragraph's content, text only.
// fill output2 with the first paragraph's content keeping the cat strong.
//
// var paragraphs = document.querySelectorAll('p');
// var new_paragraph = document.querySelector('p')
//
// paragraphs.forEach(function (e) {
//     e.innerHTML = new_paragraph.innerHTML
// });

var paragraph = document.querySelector('p');
console.log(paragraph);

var paragraph2 = document.querySelector('.output1');
console.log(paragraph2);
var paragraph3 = document.querySelector('.output2');
console.log(paragraph3);

paragraph2.textContent = paragraph.textContent;
paragraph3.innerHTML = paragraph.innerHTML;
