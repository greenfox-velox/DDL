'use strict';

var count_letters = require('./1');
var tape = require('tape');

var countBooks = require('./2');
var students = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];

var Rectangles = require('./3');
var rectangle = new Rectangles.Rectangles(3, 3);


tape (function(t) {
    t.deepEqual(count_letters.count_letters('apple'),{a: 1, p: 2, l: 1, e: 1});
    t.deepEqual(count_letters.count_letters(''),{});
    // t.throws(count_letters.count_letters(1), exception, TypeError);
    t.deepEqual(countBooks.countBooksOfStudent(students), 4);
    t.deepEqual(countBooks.countBooksOfStudent([]), 0);
    // t.throws(countBooks.countBooksOfStudent(1), exception, TypeError);
    t.deepEqual(rectangle.getCircumference(), 12);
    t.deepEqual(rectangle.getArea(), 9);
    // t.throws(countBooks.countBooksOfStudent(1), exception, TypeError);
    t.end();
});
