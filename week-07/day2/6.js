'use strict';

// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

var string = 'qwertzuiopasdfghjklyxcvbnm'


function is_element_in_array(string, letter){
    return string.indexOf(letter) !== -1;
}

console.log(is_element_in_array(string, 'a'));
console.log(is_element_in_array(string, 'é'));
