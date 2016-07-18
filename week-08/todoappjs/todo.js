'use strict';

var inputField = document.querySelector('.input-text');// querySelector-ral a documentumból input-text osztály elemet hozzárendelem az inputField változóhoz
var addButton = document.querySelector('.add-button');
//qs-ral a dokumentumból az add button osztály gombot hozzárendelem a az addbutton változóhoz
var todoContainer = document.querySelector('.todo-container');//qs-ral a documentumból a todo-container osztályú elemet hozzárendelem a todoContainer változóhoz
var host = 'https://mysterious-dusk-8248.herokuapp.com';
//a host változóhoz hozzárendelem az API url címét

function createOneNewTodo(todo) {
//létrehozok egy createOneNewTodo nevű function-t, aminek a bemeneti paramétere egy todo nevű változó
  var newLi = document.createElement('li');
// létrehozok egy newLi nevű változót, amivel a hozzárendelt a createElement metódussal létre tudok hozni egy listitem elemet
  var newDiv = document.createElement('div');
// létrehozok egy newDI változót, amivel a hozzárendelet createElement metódussal létre tudok hozni egy egy div elemet
  newDiv.setAttribute('id', 't' + todo.id);
// a newDiv változó id attributumát beállítom a setAttribute metódussal és a t stringhez hozzáfűzöm az aktuális todo id-ját
  newDiv.classList.add('text');
//a newDiv elem classList-hez hozzáadom a text ...-t
  newDiv.textContent = todo.text;
 // a newDiv elem textContent-jének beállítom a todo elem textjét (az az amit beírtunk az input mezőbe)
  newLi.setAttribute('id', 'l' + todo.id);
// a newli elem id attributumát beállítom a setAttribute metódussal és az l stringhez hozzáfűzöm az aktuális todo id-ját
  newLi.appendChild(newDiv);
// a newli elemhez hozzáadom a newdiv elemet, amiben a gombokat fogom tárolni
  todoContainer.appendChild(newLi);
// a todoContainer-hez hozzáadom a newli elemet
  var newDivForButtons = document.createElement('div');
// létrehozok egy newDivForButtons nevű változót, amivel a hozzárendelt createElement metódussal létre tudok hozni egy div elemet, ami egy gombot tartalmaz
  newLi.appendChild(newDivForButtons);
//a newli változóhoz hozzáadom a newDivForButtons elemet
  createDelButton(newDivForButtons, todo);
// létrehozom a törlés gombot a metódussal
  createcheckButton(newDivForButtons, todo);
// létrehozom a check gombot a metódussal
}

function createAllTodos(input) {
//létrehozok egy funkciót, aminek a bemeneti paramétere egy input nevű változó (az inputfielbe begépelt szöveg)
  input.forEach(function(todo) {
//az input változóra meghívom a forEach metódust, és minden inputra meghívom a createOneNewTodo metódust, aminek a bemenete a todo változó, ami megegyezik az inputtal, azaz a beírt szöveggel
    createOneNewTodo(todo);
  })
}

function getTodos() {
//létrehozok egy getTodos függvényt
  var xhr = new XMLHttpRequest();
//létrehozok egy új XMLHttpRequest példányt az xhr változóban
  var endPoint = '/todos'
// létrehozok egy endPoint nevű változót, amiben egy stringet tárolok. Ezt fogom hozzáfűzni a host változóhoz , és kettőnek a segítségével fogom megnyitni a kapcsolatot és elküldeni a GET parancsot az APInak.
  xhr.open('GET', host + endPoint);
//az xhr változóban tárolt XMLHttpRequest példány open metódusát használom a kapcsolat létrehozására. Megadom a request típusát, illetve az url címet, ahova a request-et küldöm
  xhr.setRequestHeader('content-type', 'application/json; charset=utf-8');
//itt adom meg kérés típusát, formátumát, illetve ha szükséges a privát kulcsot
  xhr.onload = function() {
//az xhr változóban tárolt XMLHttpRequest példány onload metódusát használom. Itt adom meg, hogy betöltésre, azaz a requestre/kérésre adott response/válasz megérkezésekor mi történjen. Itt a response-t JSON formátummá alakítom és betöltöm egy response változóba.
    var response = JSON.parse(xhr.response);
// a response változóval meghívom a createAllTodos metódust
    createAllTodos(response);
    };
  xhr.send();
// az xhr változóban tárolt XMLHttpRequest példány send metódusát használom, ami elküldi a requestet az APInak
}
getTodos();
//meghívom a getTodos nevű funkciót vagy metódust

function addTodo() {
//létrehozom az addTodo nevű függvényt/metódust
  var xhr = new XMLHttpRequest();
//az xhr változóban létrehozom az XMLHttpRequest objektum egy új példányát
  var endPoint = '/todos'
//létrehozom az endPoint változót, amiben egy stringet tárolok, amit hozzáfűzök a host változóban tárolt url-hez, és ezt adom majd meg az open metódus request-jének url-jeként
  xhr.open('POST', host + endPoint);
//az xhr változóban tárolt XMLHttpRequest objektum példányának open metódusát használom a kapcsolat megnyitására, létrehozására. Megadom a request típusát. illetve az url-t, ahova a requestet küldöm.
  xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
//az xhr változóban tárolt XMLHttpRequest objektum példányának a setRequestHeader metódusát használom. itt adom meg a kérés típusát/formátumát, illetva ha szükséges akkor a privátkulcsot
  var textToSend = JSON.stringify({ text: inputField.value });
//létrehozok egy textToSend változót, amiben tárolom, az inputField értékét, amit JSON formátumból a stringify metódussal stringgé/texté alakítom
  xhr.onload = function() {
//az xhr változóba töltött XMLHttpRequest objektum példányának onload metódusát használom, ami meghatározza, hogy a requestre érkezett response megérkezése, betöltődése esteén mi történjen. Ebben az esetben meghívunk egy funkciót, ami a response változóba tölti a megérkezett responseT/választ és JSON formátumuvá alakítja. Majd ezzel JSON formátumú változóval meghívja a createOneNewTodo metódust6függvényt
    var response = JSON.parse(xhr.response);
    createOneNewTodo(response);
  };
  xhr.send(textToSend);
 //az xhr változóban tárolt XMLHttpRequest objektum példányának send metódusát használom, és elküldöm vele a korábban létrehozott textToSend változót
}

addButton.addEventListener('click', addTodo);
//az addButton változóhoz hozzáadok egy eventListenert, ami clickelésre meghívja az addTodo metódust/függvényt

function createDelButton(parent, todo) {
//létrehozom a createDelButton metódust/függvényt, aminek két bemeneti paramétere van
  var del = document.createElement('button');
//a del változóban tárolok egy createElement metódust, ami egy button-t hoz létre
  del.classList.add('del-button');
// a del változóra meghívom a classList metódust és használom az add metódust, beletöltöm  a del-button osztályú elemet
  del.setAttribute('id', 'd' + todo.id);
//a del változónak a setAttribute metódus segítségével beállítom az id-ját d és a todo.id(a todo id-jának) összefűzött változatának. Tulajdonképpen új id-t hozok létre annyival, hogy a atodo id-jának elejére, ezzel a módszerrel, hozzáadok egy d stringet/karaktert
  parent.appendChild(del);
//a parent változóhoz hozzáadom a del változót (egy buttont) child-ként. A parent változó neve a chld-dal való összekapcsolás megértését próbálja segíteni. a változó lehetne bmi. Akár kiscica is, a folyamatot nem befolyásolná. AZ olvashatóságot és az érthetőséget segíti.
  del.addEventListener('click', function(event){
//a del változóban tárolt elemehez(buttonhoz), hozzáadok egy eventlistenert, ami klikkelés esetén meghív egy funkciót, ami az adott eventre/eseményre/clickelésre a következő sorokat futtatja, parancsokat hajtja végre
    delTodo(event, del.id);
//meghívja a delTodo metódust/függvényt az event és del-id paraméterekkel
  console.log(event);
//kiírja a console-ra az event értékét
  console.log(del.id);
//kiírja a console-ra a del.id értékét
  });
}

function deleteLi(event){
//létrehozom a deleteLi nevű funkciót metódust, aminek egy event nevű változó a bemeneti paramétere
  var ul = document.querySelector('ul');
//létrehozok egy ul nevű változót, amiben eltárolom a querySelector segítésgével az ul elemet
  var itemToDel = document.querySelector('#l' + event.target.id.slice(1,10));
//létrehozok egy itemToDel nevű változót, amiben eltárolom a qs meghívásával az l id-jú elemet és hozzáadom a mögötte látható borzadalmat, amivel az adott eseménykor(click), a target elem(amit törölni akarok) id-jének egyrészét(1-10) a slice metódus meghívása után, összefűzöm a korábban említett l id-val
  ul.removeChild(itemToDel);
//az ul elemre meghívom a removeChild metódust, aminek paraméterként megadom az itemToDel változót bementi paraméterként, azaz az ul elemből az itemToDel-t, amit id alapján azonosítok, törlöm.
}

function delTodo(event, delId) {
//létrehozok egy delTodo funkciót/metódust, aminek a bementi paramétere egy event és egy delID változó
  var xhr = new XMLHttpRequest();
//az xhr változóban létrehozom az XMLHttpRequest egy új példányát
  var serverId = delId.slice(1,10);
//a severID változóban eltárolom a del.id slice metódussal módosított verzióját
  var endPoint = '/todos/' + serverId;
//létrehozok egy endpoint változó, amiben egy string és a serverId változót összefűzve tárolok, amit a xhr változóban tárolt XMLHttpRequest objektum példányának open metódus meghívásakor fogok felhasználni bemeneti paraméterként
  xhr.open('DELETE', host + endPoint);
//az xhr változóban tárolt XMLHttpRequest objektum példányának open metódusát használom, aminek bemeneti paramétereként megadom a request típusát, ami ebben az esetben DELETE azaz törlés, illetve az url-t ahova a requestet küldöm, ami itt a host változó és az endpoint változó összefűzéséből áll.
  xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
//az xhr változóban tárolt XMLHttpRequest objektum példányának setRequestHeader metódusával megadom a request típusát/formátumát illetve ha szükséges itt adom meg a privátkulcsot
  xhr.onload = function() {
//az xhr változóban tárolt XMLHttpRequest objektum példányának onload metódusát használom. Ez a metódus adja meg, hogy adott requestre érkezett response megérkezése/betöltődése esetén mi történjen, mi a következő lépés a folyamatban
    deleteLi(event);
//ebben az esetben ez a lépés a deleteLi meghívása az adott event-kor. Click.
  };
  xhr.send();
//az xhr változóban tárolt XMLHttpRequest objektum példányának send metódusát használom, ami elküldi a requestet.
}

function createcheckButton(parent, todo) {
//létrehozok egy createcheckButton funkciót/metódust, aminek a két bementi paramétere a parent és todo változók
  var check = document.createElement('button');
//létrehozok egy check változót, amiben a createElement metódussal létrehozok egy buttont, gombot
  if (todo.completed) {
//ha a todo.completed igaz, azaz igaz ez az attributom, akkor a check.classList-hez az add metódussal hozzáadom a checked-button osztályt. A classList egy listát ad vissza, ami az adott elem class attributumjait listázza ki. ehhez adjuk hozzá a a checked-button osztályt, ami majd módosítja a az elem megjelenítését. az else ágon unchecked-button osztályt ad hozza, ami eszerint módosítja a megjelenését. checkre pipás kép, uncheckre üres kör.
    check.classList.add('checked-button');
  } else {
    check.classList.add('unchecked-button');
  }
  parent.appendChild(check);
//a parent elemehez az appendChild metódussal hozzáadjuk a check változóban tárolt elemet
  check.setAttribute('id', 'c' + todo.id);
//a check elemre meghívjuk a setAttribute metódust, amivel beállítjuk az id-ját. itt az id egyösszefűzött elem lesz, ami a c string/karakterbóől és todo elem idjából adódik össze.
  console.log(check.id);
//kiírom a console-ra a check elem id paraméterét
  check.addEventListener('click', function(event){
//a check elemhez hozzáadok egy eventlistenert, ami clickre meghív egy funkciót, az event esetén.
    checkTodo(event, check.id);
//itt a checkTodo metódust hívjuk meg, aminek bemeneti paramétere az event és check elem id-ja lesz.
  });
}

function changeUncheckToCheckImg(input) {
//létrehozok egy changeUncheckToCheckImg változót, egy input bementi paraméterrel.
  input.classList.remove('unchecked-button');
//az inputra meghívjuk a classlist metódust, és arra a remove metódust. Azaz, az input class attributumaninak listájából eltávolítom a zárójelben lévő unchecked-button class attributomot.
  input.classList.add('checked-button');
//az input eemre meghívjuk a classlist metódust, és meghívjuk a classlistra az add metódust. Az input elem class attributumuinak listájához hozzáadjuk a checked-button class attributumot.
}

function checkLi(event){
//létrehozok egy checkLi nevű függvényt/metódust
  var buttons = document.querySelectorAll('.unchecked-button');
//létrehozok egy buttons nevű változót, amiben eltárolom a qs_all metódus használatával az unchecked-button osztályú elemeket
  for (var i = 0; i <= buttons.length - 1; i++) {
//egy for ciklust hozok létre, létrehozom az inkremetálandó változót, beállítom a feltételt, és megadom az ikrmentálás módját és mértékét.
    if ((buttons[i]).id === event.target.id) {
//ha a buttons i-edik elemének id-ja megegyezik az esemény célpontjának id-jával(amelyik elemre kattintunk), akkor
      changeUncheckToCheckImg(buttons[i]);
//meghívjuk a changeUncheckToCheckImg metódust, aminek a bemeneti paramétere az iedik button
    }
  }
}

function getText(input, serverId){
//létrehozok egy getText nevű metódust, aminke bemeneti paraméterei az input és serverId változók.
  var divs = document.querySelectorAll('.text');
//létrehozok egy divs változót, amiben a qsall metódussal tárolom az összes text osztályú elemet
  for (var i = 0; i <= divs.length - 1; i++) {
//létrehozok egy for ciklus. létrehozom az inkrementálandó változót, megadom a feltételt, és beállítom az inkremetálás módját és mértékét
    if ((divs[i]).id === input.id) {
//ha a divs változó elemének id-ja megegyezik az inpu id-jával,
      return (divs[i]).textContent;
//akkor, visszaadja a div elemlista i-edik elemének textContent-jét
    }
  }
}

function checkTodo(event, checkId) {
//létrehozok egy checkTodo metódust, ami bemeneti paraméterként egy event és checkId változót vesz be.
  var xhr = new XMLHttpRequest();
//az xhr változóban létrehozom az XMLHttpRequest objektum egy példányát
  var serverId = checkId.slice(1,10);
//a serverID változóban a checkId slice-szal módosított változatát tároljuk***
  console.log(event.target.id.slice(1,10));
//kiiratom a console-ra, ezt a förmedvényt. Az adott esemény targetjének id-ját sliceolom, azaz a clickelt elem idjának egy részét használom fel, iratom ki.
  console.log(checkId);
//kiiratom a console-ra, a checkId-t
  console.log(checkId.slice(1,10));
//kiiratom a console-ra az id slice-olt részét
  var endPoint = '/todos/' + serverId;
//létrehozom az endpoint változót, amiben a stringhez hozzáfűzom a serverIdt. A slice levágja az elejéről az estleges string lemeket/karaktereket, így csak számok maradnka. PL c3-> 3 és így hozzá tudom fűzni az url-hez.
  console.log(endPoint);
//kiiratom az endpoint változót
  var item = document.querySelector('#t' + serverId);
//az item változóba a qs-ral kiválasztom a t id-t, amit összefűzöm a serverId változóval
  console.log(item);
//kiiratom az item változót
  var textToSend = JSON.stringify({ text: getText(item, serverId), completed: true });
//létrehozok egy textToSend változót, amiben a JSON formátumú getText metódus által visszaadott értéket stringgé alakítom
  xhr.open('PUT', host + endPoint);
//az xhr változóban tárolt XMLHttpRequest objektum példányának open metódusát meghívom, és átadom neki paraméterként a request tipusát, és az url-t ahova a request küldöm, ez au url a host és endpoint összefűzéséből áll
  xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
//az xhr változóban létrehozott XMLHttpRequest objektum példányának setRequestHeader metódusával meghatározom a request, típusát, formáját, esetlegesen megadom a privátkulcsot, ha szükséges
  xhr.onload = function() {
//az xhr változóban létrehozott XMLHttpRequest objektum példányának onload metódusával meghatározom, hogy a requestre érkezett response megérkezésekor, vagy a response betöltődése után mi fusson le, mi történjen. Itt létrehozok egy functiont, amiben meghívom a checkLi metódust/függvényt az event változóra
    checkLi(event);
  };
  xhr.send(textToSend);
//az xhr változóban létrehozott XMLHttpRequest objektum példányának send metódusát használom. ezzel elküldöm a textToSend változót requestként.
}
