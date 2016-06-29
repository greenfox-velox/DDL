// 1. Alert the content of the header.
var header_content = document.querySelector('h1')
alert(header_content.innerHTML)
// 2. Write the content of the first paragraph to the console.
var first_paragraph = document.querySelector('p')
console.log(first_paragraph.innerHTML);
// 3. Alert the content of the second paragraph.
var second_paragraph = document.querySelector('p:nth-of-type(2)')
alert(second_paragraph.innerHTML);
// 4. Replace the heading's content with 'New content'.
header_content.innerHTML = 'New Content';
console.log(header_content);
// 5. Replace the last paragraph's content with the first paragraph's content.
var last_paragraph = document.querySelector('p:nth-of-type(3)')
last_paragraph.innerHTML = header_content.innerHTML
