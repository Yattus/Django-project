// ============= MODIFIER UN ELEMENT DE LA PAGE ==============

document.getElementById('langages').innerHTML += "<li id='c'>C</li>";
// document.getElementById('langages').innerHTML = '';
//
document.querySelector('h1').textContent += " de programmation javascript";

// document.querySelector('h1').setAttribute('id', 'titre');
document.querySelector('h1').id= 'titre';

var titreElt = document.querySelector('h1');
console.log(titreElt);
titreElt.classList.remove('debut');
titreElt.classList.add('titre');
console.log(titreElt);
var pythonElt = document.createElement('li');
pythonElt.id = 'python';
pythonElt.textContent = 'Python3';
document.getElementById("langages").insertBefore(pythonElt, document.getElementById('cpp'))
var rubyElt = document.createElement('li');
rubyElt.id = 'ruby';
u = document.createElement('li');
u.id = 'ruby';
u.appendChild(document.createTextNode('Python'));
rubyElt.appendChild(u);
document.getElementById("langages").appendChild(rubyElt);

var perlElt = document.createElement('li');
perlElt.id= 'perl';
perlElt.appendChild(document.createTextNode("Perl"));
document.getElementById("langages").insertBefore(perlElt, document.getElementById('php'));

document.getElementById('langages').appendChild(document.createElement('li', document.createTextNode('Cobol')));

document.getElementById('langages').insertAdjacentHTML('afterEnd', "En voici une <a href='jfoijfoijf'>liste</a> plus complete.")
