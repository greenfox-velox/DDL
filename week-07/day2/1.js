'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"

function return_number_as_string(number){
    var numbers_in_string = ['zero', 'one', 'two', 'three', 'four'];
    if(number < 5){
        return numbers_in_string[number];
    }else{
        return 'many';
    }
}

console.log(return_number_as_string(0))
console.log(return_number_as_string(1))
console.log(return_number_as_string(2))
console.log(return_number_as_string(3))
console.log(return_number_as_string(4))
console.log(return_number_as_string(5))
console.log(return_number_as_string(6))
