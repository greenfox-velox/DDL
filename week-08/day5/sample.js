'use strict';

var fs = require('fs');

fs.readFile('alma.txt', function(err, c) {
    console.log(String(c));
    fs.writeFile('korte.text', String(c) + 'beka', function(err, c) {
    console.log('end');
    });
});
console.log('after');
//
// console.log('for elött');
//
// for (var i = 0; i < 10000000000; i++) {
//     i + 3;
// }
//
// console.log('valami');
