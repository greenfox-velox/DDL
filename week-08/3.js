'use strict';

// Create a constructor for creating Rectangles, it should take two parameters
// as the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangles(side1, side2) {
    this.side1 = side1;
    this.side2 = side2;
}

Rectangles.prototype.getArea = function() {
    var area = this.side1 * this.side2;
    return area;
}

Rectangles.prototype.getCircumference = function() {
    var circ = (this.side1 + this.side2) * 2;
    return circ;
}

var rect = new Rectangles(3, 3);
console.log(rect.getArea());
console.log(rect.getCircumference());

module.exports.Rectangles = Rectangles;
