from django.db import models

# Table pour les membres inscript
class User(models.Model):
    Nom= models.CharField(max_length= 50)
    Email= models.CharField(max_length= 50)
    date= models.DateTimeField(auto_now_add= True,
            verbose_name= "date d'inscription")

    Serie= models.ForeignKey("Serie", on_delete= models.CASCADE)
    
    def __str__(self):
        return self.Nom

# Class EXERCISE TABLE POUR LES SUJETS
class Exercise(models.Model):
    Nom= models.CharField(max_length= 50)
    serie= models.ForeignKey('Serie', on_delete= models.CASCADE)
    Cour= models.ForeignKey('Cour', on_delete= models.CASCADE)

    def __str__(self):
        return self.Nom

class Serie(models.Model):
    Nom= models.CharField(max_length= 50)

    def __str__(self):
        return self.Nom


class Cour(models.Model):
    Nom= models.CharField(max_length= 50)
    serie= models.ForeignKey("Serie", on_delete= models.CASCADE)

    def __str__(self):
        return self.Nom
