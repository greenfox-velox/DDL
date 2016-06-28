
'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {
    grades: [],
    addgrade : function(grade) {
        if(grade < 6){
            this.grades.push(grade);
        }
    },
    getAvarage : function() {
        var sum = 0;
        this.grades.forEach(function (e) {
            sum += e;
        });
        sum = sum / this.grades.length;
        // console.log(sum);
        return sum;
    }
}

student.addgrade(5);
student.addgrade(4);
student.addgrade(3);
student.addgrade(2);
student.addgrade(1);
student.addgrade(5);
student.addgrade(4);
student.addgrade(3);
student.addgrade(2);
student.addgrade(5);



console.log(student.grades);
//
console.log(student.getAvarage());


//
//
// 'use strict';
// // 1
// var car = {
//   km: 120000,
//   ride: function(km) {
//     this.km += km;
//   }
// };
//
// car.ride(220);
// console.log(car.km);
//
// // 2
// function createCar(km) {
//   return {
//     km: km,
//     ride: function(km) {
//       this.km += km;
//     }
//   };
// }
//
// var skoda = createCar(120000);
// var tesla = createCar(2000);
// tesla.ride(22);
// console.log(tesla.km);
//
// // 3
//
// function ride(km) {
//   this.km += km;
// };
//
// function Car(km) {
//   this.km = km;
//   this.ride = ride;
// }
//
// var humvee = new Car(50000);
// humvee.ride(12);
// console.log(humvee.km);
//
// var bicikli = {
//   km: 20,
//   isCool: true,
//   rideWithFeet: ride
// }
//
// bicikli.rideWithFeet(5);
// console.log(bicikli);
