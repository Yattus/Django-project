// console.log(document.body.childNodes[5].childNodes[1]);
// var titreElts = document.getElementsByTagName('h2');
// console.log(titreElts[0]);
// console.log(titreElts.length);

// if(titreElts[0]=== document.body.childNodes[5].childNodes[1]){
//     console.log('Egaux');
// }

// var merveilElts = document.getElementsByClassName('merveilles');

// for(var i= 0; i< merveilElts.length; i++){
//     console.log(merveilElts[i]);
// }

// console.log(document.getElementById('nouvelles'));

// console.log(document.querySelectorAll('#antiques > .existe').length);

// console.log(document.getElementById("contenu").innerHTML);
// console.log(document.getElementById("contenu").textContent);

// console.log(document.querySelector('a').href);

var classes = document.getElementById('antiques').classList;
console.log(classes.length);
console.log(classes[0]);

function comptElets(para){
    console.log(document.querySelectorAll(para).length);
}

comptElets('p');
