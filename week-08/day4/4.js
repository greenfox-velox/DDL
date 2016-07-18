'use strict';

// Automated CarPark system
//
// All the dates in this examples should be stored as a number
// The milliseconds lasted from 1970-01-01
//
// Create a Car constructor
// it should take 3 parameters
//  - type: the cars type as a string (eg: 'volvo')
//  - color: the cars type as a string (eg: 'red')
//  - balance: the cars parking credis as a number (eg: 500)
// every car should have an id property (a number), that is
// unique for all the cars, staeting form 0
//
// // Methods:
//
// // enter(enterDate)
// //  - it should store the date of entering
//
// // getEnterDate()
// //  - it should return the date of the last entering

// // getStats()
// //  - it should give back a string like:
// //    "Type: volvo, Color: red, Balance: 500"

// // leave(price)
// //  - it should decrease the balance with the price of the parking (that is given in an argument)
//


var id = 0;

function Car(type, color, balance){
  this.type = type;
  this.color = color;
  this.balance = balance;
  id++;
  this.id = id;
};

Car.prototype.enterDate = function(enterDate) {
  this.enterDate = enterDate;
};

Car.prototype.getEnterDate = function() {
  return this.enterDate;
};

Car.prototype.leave = function(price) {
  this.price = price;
  return this.balance - this.price;
};

Car.prototype.getStats = function() {
  console.log('Type: ' + this.type + ', Color: ' + this.color + ', Balance: ' + this.balance + ', ID ' + this.id);
};

var myauto1 = new Car('trabant','blue','120');
var myauto2 = new Car('fiat','red','120');
var myauto3 = new Car('opel','purple','120');
var myauto4 = new Car('honda','green','120');

myauto1.enterDate(16);
myauto2.enterDate(17);
myauto3.enterDate(18);
myauto4.enterDate(19);

console.log(myauto1.getEnterDate());
console.log(myauto2.getEnterDate());
console.log(myauto3.getEnterDate());
console.log(myauto4.getEnterDate());

myauto1.getStats()
myauto2.getStats()
myauto3.getStats()
myauto4.getStats()

console.log(myauto1.leave(21));
console.log(myauto2.leave(32));
console.log(myauto3.leave(14));
console.log(myauto4.leave(45));

// // Create a CarPark constructor
// // it should take 2 parameters
// //  - income: the initial credits as a number (eg: 4000)
// //  - startTime: the current date
function CarPark(income, startTime){
    self.income = income;
    self.startTime = startTime;
}
// //
// // The parking fee: 40 per hours (only every whole hour)
// //
// // Methods:
// CarPark.prototype.carEnter = function(car){}
// // carEnter(car)
// //  - It should add a car to the garage and add its stored startTime
//
// CarPark.prototpe.carLeave = function(id){}
// // carLeave(id)
// //  - It should remove the car with the given id and it should charge from its balance
//
// CarPark.prototype.elapseTime = function(hours){}
// // elapseTime(hours)
// //  - It should increment the time with the hours

// // Optional Methods:
// CarPark.prototype.getStats = function(){}
// // getStats()
// //  - It should return a string like:
// //    "Cars: 4, Time: 1234423453, Income: 1400"
//
// CarPark.prototype.getParkingCarsSince = function(hours){}
// // getParkingCarsSince(hours)
// //  - It should return the number of cars that are parking since the given hours
//
