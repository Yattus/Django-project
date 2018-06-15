from django.db import models

# Table pour les membres inscript
class User(models.Model):
    Nom= models.CharField(max_length= 50)
    Email= models.CharField(max_length= 50)
    date= models.DateTimeField(auto_now_add= True,
            verbose_name= "date d'inscription")

    Domaine= models.ForeignKey("Domaine", on_delete= models.CASCADE)
    
    def __str__(self):
        return self.Nom

# Class EXERCISE TABLE POUR LES SUJETS
class Sujet(models.Model):
    Nom= models.CharField(max_length= 50)
    Domaine= models.ForeignKey('Domaine', on_delete= models.CASCADE)
    cours= models.ForeignKey('Cours', on_delete= models.CASCADE)

    def __str__(self):
        return self.Nom

class Domaine(models.Model):
    Nom= models.CharField(max_length= 50)

    def __str__(self):
        return self.Nom

class Cours(models.Model):
    Nom= models.CharField(max_length= 50)
    Domaine= models.ForeignKey("Domaine", on_delete= models.CASCADE)

    def __str__(self):
        return self.Nom
