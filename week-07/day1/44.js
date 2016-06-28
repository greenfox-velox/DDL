'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)

function return_minimal_element(numbers){
    var min = 0
    for (var i = 0; i < numbers.length; i++){
        if (min < numbers[i]){
            min = min;
        }else if (min > numbers[i]){
            min = numbers[i]
        }
    }
    return min
}

console.log(return_minimal_element(numbers));
