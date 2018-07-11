var h= document.head;
console.log(h);

var b = document.body;
console.log(b);

if(document.body.nodeType === document.ELEMENT_NODE){
    console.log("Body est un noeud élément");
}else{
    console.log("Body est noeud Textuel");
}

for(var i= 0; i< b.childNodes.length; i++){
    console.log(b.childNodes[i]);
}

function afficherEnfant(noeud, indice){
    console.log(noeud.childNodes[indice])
}

afficherEnfant(document.body, 1);
