'use strict';

var counter = 0;
var actual_main = 0;
var actual_mini = 0;
var limit = 0;

var images = document.querySelectorAll('.mini_image_boxes img');
var image_container = document.querySelector('.mini_image_boxes');
var image_array = Array.from(images);

var main_image = document.querySelector('.pic_main');
main_image.addEventListener('click', alert_stuff);

var image_title = document.querySelector('h3');
image_title.textContent = image_array[actual_main].getAttribute('class');

var button_left = document.querySelector('.left');
button_left.addEventListener('click', scroll_left);

var button_right = document.querySelector('.right');
button_right.addEventListener('click', scroll_right);

var button_left_mini = document.querySelector('.left_mini');
button_left_mini.addEventListener('click', scroll_left_mini);

var button_right_mini = document.querySelector('.right_mini');
button_right_mini.addEventListener('click', scroll_right_mini);

function alert_stuff() {
    alert(image_title.textContent)
}

function scroll_right () {
  if (actual_main < image_array.length-1) {
    actual_main++;
    main_image.setAttribute('src', image_array[actual_main].src);
    image_title.textContent = image_array[actual_main].getAttribute('class');
  }
}

function scroll_left () {
    if (actual_main > 0) {
      actual_main--;
      main_image.setAttribute('src', image_array[actual_main].src);
      image_title.textContent = image_array[actual_main].getAttribute('class');
  }
}

function scroll_right_mini () {
  if (actual_main < image_array.length-1) {
    actual_main++;
    main_image.setAttribute('src', image_array[actual_main].src);
    image_title.textContent = image_array[actual_main].getAttribute('class');
  }
}

function scroll_left_mini () {
    if (actual_main > 0) {
      actual_main--;
      main_image.setAttribute('src', image_array[actual_main].src);
      image_title.textContent = image_array[actual_main].getAttribute('class');
  }
}
