'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

    function Stack() {
        this.element_list = [],
        this.size = function () {
            return this.element_list.length;
    },
    this.push = function(element) {
        this.element_list[this.element_list.length] = element;
    },
    this.pop = function() {
        var last_element = this.element_list[this.element_list.length-1];
        this.element_list.length--;
        return last_element;
    }
}

var stack = new Stack();
console.log(stack.size());
stack.push('One');
stack.push('Two');
stack.push('three');
stack.push('from NY');
stack.push('to Germany');
stack.push('Missing part');

console.log(stack.element_list);
console.log(stack.size());
console.log(stack.pop());
console.log(stack.size());
console.log(stack.element_list);
