'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function return_new_array_of_evens(numbers){
    var evens = []
    for(var i = 0; i < numbers.length; i++)
        if (numbers[i] % 2 === 0){
            evens += numbers[i];
        }
    return evens
}

console.log(return_new_array_of_evens(numbers));
