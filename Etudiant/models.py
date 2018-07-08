import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
# from django.utils import timezone
# Table pour les membres inscript


# Une fonction pour renommer les photo de profil
def renommage(instance):
    return "Photo_Profil/{}_{}_{}".format(instance.id,
                                          instance.user.first_name,
                                          instance.user.last_name)


# TABALE DES UTILISATEUR
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.FileField(null=True, blank=True, upload_to=renommage,
                             verbose_name="Photo de profile")

    class Meta:
        verbose_name = 'Membre'
        verbose_name_plural = 'Membres'

    def __str__(self):
        return "Salut {}".format(self.user)


# Class EXERCISE TABLE POUR LES SUJETS
class Sujet(models.Model):
    """Sujet"""
    domaine = models.ForeignKey('Domaine', on_delete=models.CASCADE)
    cours = models.ForeignKey('Cours', on_delete=models.CASCADE)
    fichier = models.FileField(upload_to="Sujets/")
    date = models.DateField(auto_now_add=False, verbose_name="Quel année ?:")
    date_d_ajout = models.DateTimeField(auto_now_add=True,
                                        verbose_name="Date de soumision")
    nb_vue = models.IntegerField(default=0, verbose_name="Nombre de vue")
    slug = models.SlugField(max_length=100)

    class Meta:
        """Meta"""
        verbose_name = "Sujet"
        verbose_name_plural = "Sujets"
        ordering = ["domaine"]

    def __str__(self):
        """__str__"""
        return "{}, Examen de {} date: {}".format(self.domaine,
                                                  self.cours, self.date)


# TABLE des domaines
class Domaine(models.Model):
    """Domaine"""
    Nom = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)

    class Meta:
        """Meta"""
        verbose_name = "Domaine"
        verbose_name_plural = "Domaines"
        ordering = ["Nom"]

    def __str__(self):
        """__str__"""
        return self.Nom


# TABLE DES COURS
class Cours(models.Model):
    """Cours"""
    Nom = models.CharField(max_length=50)
    domaine = models.ForeignKey("Domaine", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)

    class Meta:
        """Meta"""
        verbose_name = "Cours"
        verbose_name_plural = "Cours"
        ordering = ["domaine"]

    def __str__(self):
        """__str__"""
        return "{} ({})".format(self.Nom, self.domaine)


# ==============        SIDE OF MIDDLEWARE    ======================
class Page(models.Model):
    url = models.URLField()
    nb_visite = models.IntegerField(default=1)

    def __str__(self):
        return self.url


# ===================== SIDE OF SIGNALS ====================
# Signal de suppression du fichier(sujet) associer lorsqu'on efface un sujet
@receiver(pre_delete, sender=Sujet)
def sujet_sup(sender, instance, **kwargs):
    os.chdir('/home/h00a10c10k11e0r/Code/crepes/Dossiers')
    os.remove(instance.fichier.name)
    os.chdir('/home/h00a10c10k11e0r/Code/crepes/')


# signal de creation automatique d'un profil associer a chaque
# nouvel inscription
@receiver(post_save, sender=User)
def creer_user(sender, instance, **kwargs):
    # Liste des utilisateurs ayant un profil
    profil = [p.user for p in Profil.objects.all()]
    if instance not in profil:
        # Si l'instance sauvez na pas de profil on lui crée une
        Profil.objects.create(user=instance)
