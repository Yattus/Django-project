var Perso= {
    nom: "Aurora",
    vie: 100,
    force: 25,
    xp: 0,
    sante: 150,

    // Initialisation du Personnage
    init: function(nom, sante, force) {
        this.nom= nom;
        this.sante= sante;
        this.force= force;
        this.xp= 0;
    },

    // Renvoi la description du Personnage
    decrire: function(){
        var decrip= this.nom+" a "+this.sante+" point de vie, "+
            this.force+" en force et "+this.xp+"point d'experience";
        return decrip;
    }

};

var Gladuis= Object.create(Perso)

Gladuis.init("Gladuis", 180, 70);
Gladuis.puisance= "MEGA Puisance de la mort";

console.log(Perso.decrire());
console.log(Gladuis.decrire()+" & une "+Gladuis.puisance);

// var Perso2= {
//     nom: "Gladuis",
//     vie: 100,
//     force: 55,
//     xp: 0,
//     sante: 150,

//     decrire: function(){
//         var decrip= this.nom+" a "+this.sante+" point de vie, "+
//             this.force+" en force et "+this.xp+"point d'experience";
//         return decrip;
//     }
// }
