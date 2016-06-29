// Turn the party on and off by clicking the button.

//
// var button = document.querySelector('button');
// function alertGreenFox () {
//   alert('Green Fox!');
// }
// button.addEventListener('click', alertGreenFox);


var button = document.querySelector('button');
button.addEventListener('click', turnOffTheParty);


function turnOffTheParty () {
    var button = document.querySelector('div');
    button.classList.toggle('party');
}
