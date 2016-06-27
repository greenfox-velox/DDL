'use strict';

var ah = [3, 4, 5, 6, 7];
// print the sum of all numbers in ah


var sum = 0;
var i = 0;
var summa = 0;


while (i < ah.length){
    sum += ah[i];
    i++;
}

console.log(sum);



for (var j = 0; j < ah.length; j++){
    summa += ah[j];
}

console.log(summa);
