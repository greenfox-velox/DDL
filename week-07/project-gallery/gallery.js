'use strict'; // use strict meghívása, ezzel a teljes scriptre alkalmazzuk a strict mode-ot, ami jelzi a hibákat és eltéréseket a style-guide-hoz képest.

var images = [
//létrehozom az images változót, amiben listaként tárolom a képekkel kapcsolatos információkat. Nevet, számot, elérési útvonalat.
  {
    number: 'GreenFoxAcademy',
    //lista elemnek adtam számot, ami végülis nem szám, hanem név, és elérési útvonalat.
    //érdemes lenne átírnom névre, vagy hozzáadni még egy kulcsot, és a megfelelő helyre írni az értékeket
    //A többi elemre is ez igaz
    //Kipróbálhatnám, hogy hozzákötök egy expresst vagy egy adatbázist, mySQL-t v MongoDB-t
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

// itt hozom létre és illesztem a helyére a fő képet.
var currentImage = 0;
// Létrehozok egy currentImage nevű változót, amihez hozzárendelem a 0 értéket. Ezzel a változóval fogok majd iterálni.
var mainPictureContainer = document.querySelector('.pic_main');
//Létrehozom a mainPictureContainer nevű változót. Ebben fogom tárolni a főképet, amit a querrySelectorral érek el, aminek megadom az elem osztályát.
var picture = document.createElement('img');
//létrehozok egy picture változót, amiben a createElement metódust tárolom, aminek megadom a létrehiozandó elem típusát, mi img, azaz kép. Így a változó meghívásával létre tudok hozni egy kép elemet.
picture.setAttribute('src', images[0].path);
//a létrehozott picture váltóra meghívom a setAttribute metódust, amivel beállítom az src attributumát, azaz az elérési útvonalát, az images lista 0. elemének path értékét
mainPictureContainer.appendChild(picture);
//a mainPictureContainer változóban lévő pic-main osztályú elemhez hozzáadom a picture elemet, azaz beillesztek egy képet az adott helyre

// itt hozom létre és illesztem be a thumbnaileket, azaz a kisképeket
var thumbnailDiv = document.querySelector('.mini_image_boxes');
//létrehozok egy thumbnailDiv változót, ebben fogom tárolni a kisképeket/thumbnaileket. A neve is mutatja, hogy ez egy div elem lesz.
var number = document.querySelector('h3');
//létrehozok egy number változót. Ebben fogom tárolni a h3-elemet, amit a querrySelectorral érek el és rendelek ide.

function thumbIndex (i, thumbnailImages){
//létrehozok egy thumbIndex funkciót, aminek a bemeneti paramétere az i iterál, és a thumbnailImages változó.
  thumbnailImages.addEventListener('click', function () {
//a beadott thumbnailImages változóhoz hozzárendelek egy eventlistenert az addEventListener metódussal. Az event paramétere click lesz, a funkció egy anonym fuknkció, amit folytatólagosan beírok. Itt adom meg.
  picture.setAttribute('src', images[i].path);
  //a picture változóra meghívom a setAttribute metódust, attributumként az src-t adom meg, azaz az elérési útvonlat, aminek értékének az images list i-edik elemének path attribútumát adom meg.
  number.textContent =images[i].number;
  //a number változó tetxtContent attributumának értékeként beállítom az images list i-edik elemének number attribútumát
});
}
//a thumbnail kirajzolandó elemszámanak korlátozása
for (var i = 0; i < 4 ;i++){
//létrehozok egy for ciklust. iterálként
  var thumbnailImages = document.createElement('img');
  //létrehozok egy thumbnailImages változót, amihez hozzárendelem a createElement metódust az img attribútummal, azaz ezzel a változóval kép-elemet tudok majd létrehozni
  thumbnailImages.setAttribute('src', images[i].path);
  //a thumbnailImages változóra meghívom a setAttribute metódust, és beáálítom az src, azaz az elérési útvonal attributumát az images lista i-edik elemének path attributumára.
  thumbnailDiv.appendChild(thumbnailImages);
  //a thumbnailDiv változóban tárolt div elemre meghívom az appendchild metódust a thumbnailImages attributummal.
  thumbIndex(i, thumbnailImages);
  //meghívom a thumbIndex funkciót, aminek bemeneti attributumai az i iterál, és a thumbnailImages elem.
}

// a főkép megváltoztatása másik galériában lévő képre.
function getNewPic() {
//létrehozom a getNewPic metódust/függvényt
  var mainImage = document.querySelector('.pic_main img');
  //létrehozom a mainImage változót, amiben a pic_main osztályú elemben lévő img elemet fogom tárolni. A querySelector metódust használom ahhoz, hogy elérjem az elemet.
  mainImage.setAttribute('src', images[currentImage].path);
  //a mainImage változóra meghívom a setAttribute metódust, amivel az src attributumát, azaz elérési útvonal attributumát fogom beállítani az images lista currentImage-edik elemének (a currentImage egy int tipusú számot tárol) path attributumával megegyezőre.
  number.textContent = images[currentImage].number;
  //a number elem textContent attributumához hozzárendelem az images list currentImage-edik elemének number attributumát
}


// a főkép indexének növelése, csökkentése
function nextImage() {
// létrehozok egy nextImage változót
  if (currentImage < images.length - 1) {
//if elágazást használva, ha currentImage kisebb, mint az images lista hossza-1 feltétel teljesül, akkor
    currentImage++;
    // a currentImage váltózó értékét inkrementálom
  } else {
    //ha nem teljesül a feltétel, akkor a currentImage értéke 0 lesz. Ez a feltétel teszi lehetővé, hogy a képek körbemenjenek. Ennek az ágnak a kivétele esetén a képek megállnánaka a legnagyobb indexű képnél, azaz azt utolsó képnél.
    currentImage = 0;
  }
}

function prevImage() {
//létrehozok egy prevImage függvényt/metódust
  if (currentImage > 0) {
//if elágazást használok. Feltételként megadom, hogy a currentImage értéke nagyobb, mint 0.
    currentImage--;
    //ha teljesül a feltétel, akkor a currentImage értékét dekrementálom
  } else {
    //ha nem teljesül a feltétel
    currentImage = images.length - 1;
    //a currentImage értékét az images lista hossza-1 értékkel teszem egyenlővé. Így a lista körbejár. Enélkül megállna az első indexű képnél a lapozás.
  }
}

// add click events to main next & prev buttons
//kattintás esemény hozzáadása a főkép következő és előző gombokhoz
var next = document.querySelector('.right_side_arrow');
//létrehozok egy next változót és hozzárendelem a right_side_arrow osztályú elemet a querySelector metódus használatával
next.addEventListener('click', function() {
//a next változóra meghívom az addEventListener metódust, és bementi paraméterként megadom neki a click attributumot, valamint egy anonym függvényt, amiben meghívom a nextImage és getNewPic függvényeket/metódusokat
  nextImage();//ezt feljebb kifejtettem
  getNewPic();//ezt feljebb kifejtettem
});

var prev = document.querySelector('.left_side_arrow');
//létrehozom a prev nevű változót és hozzárendelem a left_side_arrow osztály elemét a querrySelectorral.
prev.addEventListener('click', function () {
//a prev változóra meghívom az addEventListener metódust és bemeneti paraméterként megadom neki a click attributumot, és egy anonym függvényt, amiben meghívom a prevImage és getNewPic függvényeket/metódusokat
  prevImage();//ezt feljebb kifejtettem
  getNewPic();//ezt feljebb kifejtettem
});

// thumbnail
var thumbImage = 0;
//létrehozok egy változót thumbImage névvel, amihez a 0 értéket rendelem
function slide() {
//létrehozok egy funkciót slide névvel.
  for (var i = thumbImage; i < thumbImage + 4; i++) {
//for ciklust használok. Létrehozom az iterált változóként, amihez hozzárendelem a thumbImage értékét. Feltételként megadom, hogy az iterál/i legyen kisebb a thumbImage + 4 értéknél, és megadom az inkrementálást.
    var thumbnailImages = document.createElement('img');
    //létrehozok egy thumbnailImages változót, amihez hozzárendelem a createElement metódust z img attributummal. Így a változó meghívásakor létrehozunk egy kép-elemet.
    thumbnailImages.setAttribute('src', images[i].path);
    //a thumbnailImages változóra meghívom a setAttribute metódust, és az src attributumát beállítom az images list iedik elemének path értékére, azaz elérési útjára.
    thumbnailDiv.appendChild(thumbnailImages);
    //a thumbnailDiv elemhez az appendChild metódussal hozzáadom a thumbnailImages elemet.
    addtoThumbnails(i, thumbnailImages);
    //meghívom az addtoThumbnails metüdust/függvényt, aminek bemeneti paraméterként megadom az i iterált és a thumbnailImages változóban tárolt elemet.
  }
}

function addtoThumbnails(i, thumbnailImages) {
//létrehozok egy addtoThumbnails függvényt/metódust, aminek bementi parméterei az i iterál/index/változó és a thumbImages változóban lévő elem.
  thumbnailImages.addEventListener('click', function () {
//a thumbnailImages változóra meghívom az addEventListener metódust, aminek paramétereként megadom a click attributumot és egy anonym függvényt. Így kattintásra következő események következnek be:
    picture.setAttribute('src', images[i].path);
    //a picture változóra meghívom a setAttribute metódust, aminek paraméterként megadom az src attributumot, és beállítom neki értékként az images list i-edik elemének path értékét, azaz hozzárnedelem az elérési útvonalat.
    number.textContent = images[i].number;
    //a number elem textContent paraméteréhez hozzárendelem az image lista number értékét
  });
}

//a thumbnail képek indexének növelése illetve csökkentése, és körbefutattása
function nextThumb() {
//létrehozok egy nextThumb nevű metódust/függvényt
  if (thumbImage + 4 < images.length - 1) {
//elágazást használok. Ha thumbImage + 4 értéke kisebb mint az images lista-1, akkor:
    thumbImage++;
    //a thumbImage értékét inkrementálom
  }
}

function prevThumb() {
//létrehozok egy prevThumb függvényt/metódust
  if (thumbImage > 0) {
//ha a thumbImage nagyobb, mint 0, akkor
    thumbImage--;
    //dekrementálom a thumbImage értékét.
  }
}

//klik esemény hozzáadása a thumbnail következő és előző gombjaihoz
var thumbNext = document.querySelector('.right_side_arrow_mini');
//létrehozok egy változót, amihez hozzárendelem a a right_side_arrow_mini osztályú elemet a querrySelectorral.
thumbNext.addEventListener('click', function () {
//a thumbNext változóra meghívom az addEventListener metódust, és paraméterként megaadok neki egy anonym funkciót, amiben
  thumbnailDiv.innerHTML = '';
  //a thumbnailDiv innerHTML értékéhez egy üres stringet rendelek és meghívom a nextThumb és slide metódusokat/függvényeket.
  nextThumb();//ezt feljebb kifejtettem
  slide();//ezt feljebb kifejtettem
});

var thumbPrev = document.querySelector('.left_side_arrow_mini');
//létrehozom a thumPrev változót és hozzárendelem a left_side_arrow_mini osztályú elemet a querySelectorral
thumbPrev.addEventListener('click', function () {
//a thumbPrev változóra meghívom az addEventListener metódust és bementi paraméterként megadom neki a click attributumot és egy anonym függvényt, amiben,
  thumbnailDiv.innerHTML = '';
  //a thumbnailDiv innerHTML értékéhez hozzárendelek egy üres striget, és meghívom a prevThumb és slide függvényeket/metódusokat.
  prevThumb();//ezt feljebb kifejtettem
  slide();//ezt feljebb kifejtettem
});
