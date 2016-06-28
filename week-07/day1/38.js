'use strict';

// Write a program that prints the numbers from 1 to 100.
// But for multiples of three print "Fizz" instead of the number
// and for the multiples of five print "Buzz".
// For numbers which are multiples of both three and five print "FizzBuzz".


var a = 1;

while (a <= 100) {
    if (a % 15 === 0) {
        console.log('FizzBuzz');
    } else if (a % 3 === 0) {
        console.log('Fizz');
    } else if (a % 5 === 0) {
        console.log('Buzz');
    } else {
        console.log(a);
    }
    a++
}


 for (var b = 0; b <= 100; b++) {
    if (b % 3 == 0 || b % 5 == 0) {
        console.log('FizzBuzz');
    } else if (b % 3 == 0) {
        console.log('Fizz');
    } else if (b % 5 == 0) {
        console.log('Buzz');
    } else {
        console.log(b);
    }
}
