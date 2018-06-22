from django.db import models
# from django.utils import timezone
# Table pour les membres inscript
class User(models.Model):
    Nom = models.CharField(max_length=50)
    Email= models.CharField(max_length= 50)
    date= models.DateTimeField(auto_now_add= True,
            verbose_name= "date d'inscription")

    domaine= models.ForeignKey("Domaine", on_delete= models.CASCADE)

    class Meta:
        verbose_name= "Membre Inscrit"
        verbose_name_plural= "Membres Inscrits"
        ordering= ['domaine']

    def __str__(self):
        return self.Nom

# Class EXERCISE TABLE POUR LES SUJETS
class Sujet(models.Model):
    domaine= models.ForeignKey('Domaine', on_delete= models.CASCADE)
    cours= models.ForeignKey('Cours', on_delete= models.CASCADE)
    file= models.FileField(upload_to= "Sujets/")
    date = models.DateField(auto_now_add=False, verbose_name="Quel année ?:")
    date_d_ajout= models.DateTimeField(auto_now_add= True, verbose_name= "Date de soumision")
    nb_vue= models.IntegerField(default= 0, verbose_name= "Nombre de vue")

    class Meta:
        verbose_name= "Sujet"
        verbose_name_plural= "Sujets"
        ordering= ["domaine"]

    def __str__(self):
        return "{}, Examen de {} date: {}".format(self.domaine, self.cours, self.date)

class Domaine(models.Model):
    Nom= models.CharField(max_length= 50)

    class Meta:
        verbose_name= "Domaine"
        verbose_name_plural= "Domaines"
        ordering= ["Nom"]

    def __str__(self):
        return self.Nom

class Cours(models.Model):
    Nom= models.CharField(max_length= 50)
    domaine= models.ForeignKey("Domaine", on_delete= models.CASCADE)

    class Meta:
        verbose_name= "Cours"
        verbose_name_plural= "Cours"
        ordering= ["domaine"]

    def __str__(self):
        return "{} ({})".format(self.Nom, self.domaine)
