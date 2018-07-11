var Personne= {
    initPerso: function(nom, sante, force){
        this.nom= nom;
        this.sante= sante;
        this.force= force;
	},

    attaquer: function(cible){
        if(this.sante> 0){
            console.log(this.nom+" attaquer "+cible.nom+" et lui fait "+this.force+" point de degats");
            cible.sante-= this.force;
            if(cible.sante> 0){
                console.log(cible.nom+" a encore "+cible.sante+" point de vie");
            }
            else{
                cible.sante = 0;
                console.log(cible.nom+" est mort !");
            }
        }

        else{
            console.log(this.nom+" ne peut pas attaquer : il est mort...");
        }

    }
};

var Joueur= Object.create(Personne);

Joueur.combattre= function(advers){
    this.attaquer(advers);
    if(advers.sante=== 0){
        console.log(this.nom+" a tue "+advers.nom+" et gagne "+ advers.valeur+" points d'experience");
        this.xp+= advers.valeur;
    }
}

Joueur.initJoueur= function(nom, sante, force){
    this.initPerso(nom, sante, force);
    this.xp= 0;
};

Joueur.decrire= function(){
    var descrip= this.nom+" a "+this.sante+" points de vie, "+this.force+" en force et "+this.xp+" points d'experience";
    return descrip;
};

var Adversaire= Object.create(Personne);

Adversaire.initAdversaire= function(nom, sante, force, race, valeur){
    this.initPerso(nom, sante, force);
    this.race= race;
    this.valeur= valeur;
};

var j1= Object.create(Joueur);
j1.initJoueur('Aurora', 150, 25);

var j2= Object.create(Joueur);
j2.initJoueur('Gladuis', 130, 30);

console.log("Bienvenu dans ce jeu d'avanture! Voici nos courageux heros :");
console.log(j1.decrire());
console.log(j2.decrire());

var monstre= Object.create(Adversaire);
monstre.initAdversaire("ZogZog", 40, 20, "orc", 10);

console.log("Un affreux monstre arrive: c'est un "+monstre.race+" nomme "+monstre.nom);

monstre.attaquer(j1);
monstre.attaquer(j2);

j1.combattre(monstre);
j2.combattre(monstre);

console.log(j1.decrire());
console.log(j2.decrire());
