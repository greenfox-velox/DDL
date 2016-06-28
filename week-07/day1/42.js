
'use strict';

// create a function that returns it's input factorial

function return_factorial(number){
    var fact = 1;
    for (var i = 1; i <= number; i++){
        fact *= i;
    }
    return fact
}

console.log(return_factorial(5));
