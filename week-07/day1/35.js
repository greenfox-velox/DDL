'use strict';

var ah = ['kuty', 'macsk', 'cic']
// add to all elements an 'a' on the end

var i = 0;

while (i < ah.length){
    ah[i] += 'a'
    i++
}

console.log(ah);


for (var j = 0; j < ah.length; j++ ){
    ah[j] += 'ci'
}

console.log(ah);
