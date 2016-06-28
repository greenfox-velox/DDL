
'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function


function my_own_sumFun(list_of_numbers){
    var sum = 0
    for(var i = 0; i < list_of_numbers.length; i++ ){
        sum += list_of_numbers[i];
        console.log(list_of_numbers[i]);
    }
    console.log(sum);
}

my_own_sumFun(numbers);
