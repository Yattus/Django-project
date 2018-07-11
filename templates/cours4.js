var pElt = document.querySelector("p");
pElt.style.color = 'red';
pElt.style.margin = '50px';
pElt.style.fontFamily = 'Arial';
pElt.style.backgroundColor = "yellow";

var pElts = document.querySelectorAll('p');
console.log(pElts[0].style.color);
console.log(pElts[1].style.color);
console.log(getComputedStyle(pElts[2]).color);
