'use strict';

// create a function called apply that takes a function and calls it with one argument
// that is the string 'apple'

// apply(console.log) // should log apple

function apply(func, arg){
    func(arg);
}

apply(console.log, 'apple'); // should log apple
