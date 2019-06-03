from django.db import models

# Create your models here.
class Chanson(models.Model):
        groupe    = models.CharField(max_length=50) 
        titre  = models.CharField(max_length=50)  
        youtube = models.URLField(max_length=100, default='', blank=True)
        categorie = models.ManyToManyField('appsong.Categorie')
        def __str__(self):
            return str(self.titre)
        
class Categorie(models.Model):
        nom = models.CharField(max_length=30)
        def __str__(self):
           return str(self.nom)
        
class Texte(models.Model):
        chanson = models.OneToOneField('appsong.Chanson', primary_key=True,
                   on_delete=models.CASCADE)
        paroles = models.TextField(max_length=10000)

class Utilisateur(models.Model):
        pseudo = models.CharField(max_length=20)
        password = models.CharField(max_length=20)
        
class Commentaire(models.Model):
        title = models.CharField(max_length= 100)
        body =  models.CharField(max_length= 100)
        def __str__(self):
                return self.title 

        class Meta:
                ordering = ('title',)