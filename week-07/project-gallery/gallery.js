'use strict';

var images = [
  {
    number: 'GreenFoxAcademy',
    path: 'images/fox.png',
  },
  {
    number: 'Github',
    path: 'images/github_.png',
  },
  {
    number: 'HTML5',
    path: 'images/html5.png',
  },
  {
    number: 'CSS3',
    path: 'images/css3.png',
  },
  {
    number: 'Python3',
    path: 'images/python.png',
  },
  {
    number: 'Javascript',
    path: 'images/js.png',
  },
  {
    number: 'Google',
    path: 'images/google_.png',
  },
  {
    number: 'Stackoverflow',
    path: 'images/stackoverflow_.png',
  },
  {
    number: 'Databases',
    path: 'images/database.png',
  },
];

// create and insert main image
var currentImage = 0;
var mainPictureContainer = document.querySelector('.pic_main');
var picture = document.createElement('img');
picture.setAttribute('src', images[0].path);
mainPictureContainer.appendChild(picture);

// create and insert thumbnail images
var thumbnailDiv = document.querySelector('.mini_image_boxes');
var number = document.querySelector('h3');

images.forEach(function (e) {
  var thumbnailImages = document.createElement('img');
  thumbnailImages.setAttribute('src', e.path);
  thumbnailDiv.appendChild(thumbnailImages);
  // add click function to thumbnail images
  thumbnailImages.addEventListener('click', function () {
    picture.setAttribute('src', e.path);
    number.textContent = e.number;
  });
});

// switch main image with other images in the gallery list
function getNewPic() {
  var mainImage = document.querySelector('.pic_main img');
  mainImage.setAttribute('src', images[currentImage].path);
  number.textContent = images[currentImage].number;
}

// cycle through the main images, index increse/decrease
function nextImage() {
  if (currentImage < images.length - 1) {
    currentImage++;
  } else {
    currentImage = 0;
  }
}

function prevImage() {
  if (currentImage > 0) {
    currentImage--;
  } else {
    currentImage = images.length - 1;
  }
}

// add click events to main next & prev buttons
var next = document.querySelector('.right_side_arrow');
next.addEventListener('click', function() {
  nextImage();
  getNewPic();
});

var prev = document.querySelector('.left_side_arrow');
prev.addEventListener('click', function () {
  prevImage();
  getNewPic();
});

// thumbnail
var thumbImage = 0;
function slide() {
  for (var i = thumbImage; i < thumbImage + 4; i++) {
    var thumbnailImages = document.createElement('img');
    thumbnailImages.setAttribute('src', images[i].path);
    thumbnailDiv.appendChild(thumbnailImages);
    addtoThumbnails(i, thumbnailImages);
  }
}

function addtoThumbnails(i, thumbnailImages) {
  thumbnailImages.addEventListener('click', function () {
    picture.setAttribute('src', images[i].path);
    number.textContent = images[i].number;
  });
}


// // cycle through the thumbnail images, index increse/decrease
function nextThumb() {
  if (thumbImage + 4 < images.length - 1) {
    thumbImage++;
  }
}

function prevThumb() {
  if (thumbImage > 0) {
    thumbImage--;
  }
}

// add click events to thumbnail next & prev buttons
var thumbNext = document.querySelector('.right_side_arrow_mini');
thumbNext.addEventListener('click', function () {
  thumbnailDiv.innerHTML = '';
  nextThumb();
  slide();
});

var thumbPrev = document.querySelector('.left_side_arrow_mini');
thumbPrev.addEventListener('click', function () {
  thumbnailDiv.innerHTML = '';
  prevThumb();
  slide();
});
