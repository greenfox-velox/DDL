// Remove the king from the list.

var ul_list = document.querySelector('.asteroids');
var the_king = document.querySelector('li');
ul_list.removeChild(the_king);

// Fill the list based on the following list of objects:

var planetData = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true
  }
]
// only add the asteroids to the list.
// each list item should have its category as a class
// and its content as text content.

planetData.forEach(function (e) {
    if (e['asteroid']) {
        var newLi = document.createElement('li');
        newLi.textContent = e['content'];
        newLi.classList.add(e['category']);
        ul_list.appendChild(newLi);
    }
});
