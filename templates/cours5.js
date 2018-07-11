var boutonEtl = document.getElementById('bouton');
var boutonetl = document.getElementById('Bouton');
var cp = 0;
function clic () {
    cp+= 1;
    console.log(cp);
};
function clicc () {
    cp = 0;
    console.log(cp);
};

boutonEtl.addEventListener('click', clic);
boutonetl.addEventListener('click', clicc);

// boutonEtl.addEventListener('click', function (e) {
//     console.log('Evenement:'+ e.type +
//         ', texte de la cible :' + e.target.textContent);
// });

// document.addEventListener('keypress', function(e){
//     console.log("Vous avez appuyer sur la touche "+String.fromCharCode(e.charCode));
// })

// function infosClavier(e){
//     console.log("Evenement clavier :"+e.type+', touche :'+e.keyCode);
// }

// document.addEventListener('keydown', infosClavier);
// document.addEventListener('keyup', infosClavier);

// function getBoutonSouris(code){
//     var bouton = 'inconnu';
//     switch (code){
//          case 0:
//             bouton = 'gauche';
//             break;
//          case 1:
//             bouton = 'milieu';
//             break;
//          case 2:
//             bouton = 'droit';
//             break;
//     }
//     return bouton;
// }

// function infosSouris(e){
//     console.log("Evenement souris :"+e.type+', bouton'+
//     getBoutonSouris(e.button)+", X :"+e.clientX+", Y : "+e.clientY);
// }

// document.addEventListener('click', infosSouris);
// document.addEventListener('mousedown', infosSouris);
// document.addEventListener('mouseup', infosSouris);

// window.addEventListener('load', function(){
//     console.log('Page entierement chargée');
// });

// window.addEventListener('beforeunload', function(e){
//     var message = "On est bien ici !";
//     e.returnValue = message;
//     return message;
// });

// document.addEventListener('click', function(){
//     console.log("Gestionnaire document");
// });

// document.getElementById("para").addEventListener('click', function(){
//     console.log("Gestionnaire paragraphe");
// });

// document.getElementById("propa").addEventListener('click', function(e){
//     console.log('Gestionnaire bouton');
//     e.stopPropagation();
// });

// document.getElementById('interdit').addEventListener('click', function(e){
//     console.log("Continuez plutôt à lire le cours ;)");
//     e.preventDefault();
// });
