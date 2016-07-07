'use strict';

var yButton = document.querySelector('button');
yButton.addEventListener('click', yodanize);
var result = document.querySelector('p');


function yodanize() {
  console.log('Hello');
  var xhr = new XMLHttpRequest();
  var input = document.querySelector('.input_text');

  var text = input.value;
  var url = 'https://yoda.p.mashape.com/yoda?sentence=';
  var urlResult = url + encodeURIComponent(text);
  xhr.open('GET', urlResult);
  xhr.setRequestHeader("X-Mashape-Key",  "tic9M4Iz2FmshcI5RvLVTGVqAzAgp1MprXmjsnnfFJ0G0TqIFJ");
  xhr.onreadystatechange = function () {
      if (xhr.readyState == 4) {
          result.textContent = xhr.response
      };
    };
  xhr.send();
}
