from django.forms.widgets import HiddenInput
from django import forms
from .models import *

class SaisieChansonForm(forms.Form):
    groupe  = forms.CharField(label='Groupe', max_length=50)
    titre  = forms.CharField(label='Titre', max_length=50)
    youtube = forms.CharField(label='youtube', required=False)
    paroles = forms.CharField (
        label="Paroles", 
        widget=forms.Textarea(
            attrs={'cols': '90', 'rows': '10', 'class': 'saisie-paroles'}),
        required=False)
    #deplacement = forms.ModelChoiceField(label='Déplacement', 
     #       queryset=Deplacement.objects.all().order_by('id'), empty_label=None)

class ModifCategorieForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=20)
    cate_id = forms.IntegerField(widget=HiddenInput())   
    
class AddCategorieForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=20)

class ConnexionForm(forms.Form):
    pseudo = forms.CharField(label='Pseudo', required= True)
    password = forms.CharField(label='Password', widget= forms.PasswordInput, required= True)
 
class EnregistrementForm(forms.Form):
    pseudo = forms.CharField(label='Pseudo', required= True)
    password = forms.CharField(label='Password', widget= forms.PasswordInput, required= True)
    password2 = forms.CharField(label='password2', widget= forms.PasswordInput, required= True)
   
class CategorieChansonForm(forms.Form):
    nom = forms.ModelChoiceField(label='Nom',
     queryset = Categorie.objects.all().order_by("id"),empty_label=None)

'''
class SearchForm(forms.Form):
     cate_filters =  forms.ModelMultipleChoiceField(label = 'Catégorie' '''

class SelectSongForm(forms.Form):
    #titreOrGroupe = forms.CharField(label = 'Titre ou groupe', max_length=20,required=False)
    #faire une liste deroulente
    categorie = forms.CharField(label = 'Catégorie', max_length=20,required=False)

class CommentaireForm(forms.Form):
    Texte = forms.CharField(label='Texte', max_length=20)
