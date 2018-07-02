var Personne= {
    nom: "Aurora",
    vie: 100,

    decrire: function(){
        description= "Je suis "+this.nom+" j'ai "+this.vie+" vie";
        return description;
    }
};

// OU

var Perso= {};
Perso.nom= "Machin";
Perso.vie= 100;
Perso.force= 50;

Perso.decrire= function(){
        description= "Je suis "+Perso.nom+" j'ai "+Perso.vie+" vie et "+Perso.force+" force";
        return description;
};

// var Truck= new Perso2();

var o= Perso.decrire();
console.log(o);
var r= Personne.decrire();
console.log(r);

function decrire(Perso){
        description= "Je suis "+Perso.nom+" j'ai "+Perso.vie+" vie et "+Perso.force+" force";
        return description;
};
console.log(decrire(Perso))
