#import json
from django.shortcuts import render,redirect
from django.urls import reverse
from appsong.models import *
from django.http import HttpResponse
from appsong.forms import * 
from django.forms.formsets import formset_factory
from django.contrib import messages 
from django.shortcuts import render
from django.db.models import Q


"""
#<-----------------OLD FONCTIONS--------------------->
    def charger_json(filename):
        try:
            a = open(filename,"r")
            d = json.load(a)
            a.close()
            return d
        except(FileNotFoundError,json.decoder.JSONDecodeError):
        return None

    def  chercher_chanson (catalogue, chanson_id):
        #cherche dans catalogue la chanson dont id vaut chanson_id.
        for element in catalogue :
            if element.id == str(chanson_id):
                return element
        return None

    def charger_paroles(chanson):
        f = open("appsong/paroles/"+chanson["fichier"],"r")
        s = f.read()
        f.close()
        return s
    """

#<-----------------PAGE PRINCIPALE---------------->
# TO FINISH
def gen_page_principale(request):
    context = {
        'titre' : 'Catalogue de chansons',
        'catalogue' : Chanson.objects.all(),
        'categorie' : Categorie.objects.all(),
        'url_nouv_chanson' : reverse ('appsong:nouv_chanson'), 
        'url_gerer_cate' : reverse ('appsong:gerer_cate'), 
        'request' : request,
    } 
    ''' if request.method == 'POST' :
            regex = request.GET.get("regex", "")
            cats = request.GET.getlist('cats', '')
        else:
            regex = ''
            cats = []

        songs = Chanson.objects.all()
        songs = filter_songs(songs, regex, cats)

        context = {
            'songs' : songs,
            'cats' : Categorie.objects.all(),
            'query': [regex, cats, len(cats)>0]
        }'''
    return render (request, 'appsong/principale.html', context)

'''
def filter_songs(songs, regex, cats):

    if len(cats)>0:
        songs_filtered = []
        for song in songs:
            for cat_filter in song.categories.all():
                for cat in cats:
                    if cat == cat_filter.nom and song not in songs_filtered:
                        songs_filtered.append(song)
    else:
        songs_filtered = songs

    return songs_filtered'''

#<-------------------CHANSON--------------------------->
#DONE
def gen_page_chanson(request, chanson_id):
    # Captez l'exception Chanson.DoesNotExist
    try: 
        parole = Texte.objects.get(chanson_id=chanson_id)
    except Texte.DoesNotExist:
        pass 

    context = {
        'chanson_id' : chanson_id, 
        'chanson' : Chanson.objects.get(id=chanson_id),
        'categorie' : Categorie.objects.all(),
        'parole' : parole,
        'url_page_princ' : reverse ('appsong:page_princ')
    }

    return render (request, 'appsong/chanson.html', context)

#DONE
def gen_nouv_chanson(request):
    context = {
            'titre'   : "Nouvelle chanson",
            'url_page_princ' : reverse ('appsong:page_princ'),
            'request' : request,    # pour debug
        }
    if request.method == 'POST' :
        form = SaisieChansonForm(request.POST)
        if form.is_valid() :
            groupe   = form.cleaned_data['groupe']
            titre = form.cleaned_data['titre']
            youtube = form.cleaned_data['youtube']
            parole = form.cleaned_data['paroles']
            # puis enregistrer dans la base
            liste = Chanson.objects.filter(groupe__iexact=groupe, titre__iexact=titre)
            if len(liste) == 0 :
                # Enregistrement dans la base
                nouv = Chanson()
                nouv.groupe = groupe
                nouv.titre = titre
                nouv.youtube = youtube
                nouv.save()
                new = Texte(chanson_id=nouv.id)
                new.paroles = parole  
                new.save()
                context['nc_message'] = 'Chanson enregistré avec succès.'
            else :
                context['nc_message'] = 'Erreur : chanson déjà dans la base.'
    else:
        form = SaisieChansonForm()
    context['nc_form'] = form
    return render(request, 'appsong/nouv_chanson.html', context)

#DONE
def gen_modif_chanson(request, chanson_id):    
    liste=Chanson.objects.filter(id=chanson_id)
    texte = Texte.objects.filter(chanson=chanson_id)
    context = {
        'url_page_princ' : reverse ('appsong:page_princ'),
        'titre' : 'Modifier Chanson',
        'request' : request,
    }
    print(len(liste))
    if (len(liste)==1):
        context['chanson_id'] = chanson_id
        data = {
            'groupe' : liste[0].groupe,
            'titre' : liste[0].titre,
            'youtube' : liste[0].youtube,
        }
        try:    
            data['paroles']= texte[0].paroles
        except IndexError:
            data['paroles'] = None
        if request.method=='POST':
            form = SaisieChansonForm(request.POST)
            if form.is_valid() :
                if "b_supp" in request.POST:
                    chanson=Chanson.objects.get(id=chanson_id)
                    chanson.delete()
                    return redirect(reverse('appsong:page_princ'))
                    #context['mc_message'] = 'Chanson supprimé'
                elif "b_modifier" in request.POST:
                    groupe   = form.cleaned_data['groupe']
                    titre  = form.cleaned_data['titre']
                    youtube = form.cleaned_data['youtube']
                    paroles = form.cleaned_data['paroles']
                    chanson=Chanson.objects.get(id=chanson_id)
                    chanson.groupe = groupe
                    chanson.titre = titre
                    chanson.youtube = youtube
                    chanson.save()
                    texte = Texte.objects.get(chanson_id=chanson_id)
                    texte.chanson_id = chanson_id               
                    texte.paroles = paroles
                    texte.save()					       
                    context['mc_message'] = 'Chanson modifié avec succès.'
                

        else:
            form = SaisieChansonForm(data)
            context['mc_form'] = form 
    else :
        context['mc_message'] = 'Erreur : chanson pas dans la base.'
    return render(request, 'appsong/modif_chanson.html', context)

#DONE
def gen_cate_of_chanson(request, chanson_id):
    chanson=Chanson.objects.filter(id=chanson_id)  
    if (len(chanson)==1):
        context = {
            'titre' : 'categorie de ',
            'chanson' : chanson, 
            'chanson' : Chanson.objects.get(id=chanson_id),
            'url_page_princ' : reverse ('appsong:page_princ'),
            'request': request,
        }
        if request.method == 'POST':
            form = CategorieChansonForm(request.POST)
            if form.is_valid():
                if 'b_add' in request.POST:
                    nom = form.cleaned_data['nom']
                    nouv = Chanson.objects.get(id=chanson_id)
                    nouv.categorie.add(nom)
                    nouv.save()
                    #return redirect(reverse('appsong:page_chanson'))
                    context['cc_message'] = ' Catégorie ajouté '
                elif 'b_suppr' in request.POST:
                    nom = form.cleaned_data['nom']
                    nouv = Chanson.objects.get(id=chanson_id)
                    nouv.categorie.remove(nom)
                    # return redirect(reverse('appsong:page_chanson'))
                    context['cc_message'] = 'Catégorie supprimé'
        else:
            form = CategorieChansonForm()
            context['cc_form'] = form
    else :
        context['coc_message'] = 'Erreur : chanson pas dans la base.'

    return render(request, 'appsong/cate_of_chanson.html', context)

#<--------------- GERER CATEGORIE---------------------->
#DONE
def gen_page_cate(request):
    context = {
        'titre' : 'Gérer les catégories',
        'url_add_cate' : reverse ('appsong:add_cate'),
        'url_page_princ' : reverse ('appsong:page_princ'),
        'categorie' : Categorie.objects.all(),
        'request' : request, # pour debug
    }

    return render(request, 'appsong/gerer_cate.html', context)

#DONE
def delete(request,cate_id):

    cate = Categorie.objects.get(id=cate_id)
    cate.delete()
    return redirect(reverse('appsong:gerer_cate'))
    
#DONE
def gen_add_cate(request):
        context={
            'titre' : 'Ajout de catégorie',
            'categorie' : Categorie.objects.all(),
            'url_page_princ' : reverse ('appsong:page_princ'),
            'request' : request, #pour debug
        }
        if request.method == 'POST':
            form = AddCategorieForm(request.POST)
            if form.is_valid():
                nom = form.cleaned_data['nom']

                liste = Categorie.objects.filter(nom__iexact = nom)
                if len(liste)== 0:
                    nouv = Categorie()
                    nouv.nom = nom
                    nouv.save()
                    return redirect(reverse('appsong:add_cate'))
                    #context['ac_message'] = 'Categorie ajouté'
                else:
                    context['ac_message'] = 'Catégorie déjà existante'
        else: 
            form = AddCategorieForm()
            context['ac_form'] = form
        return render(request, 'appsong/add_cate.html', context)

#<------------------UTILISATEUR------------------------>
#DONE
def gen_page_connexion(request) :
    # rajout , utilisateur en parametre
    # On stocke l'utilisateur dans la session
    # request.session['utilisateur'] = utilisateur
    context = {            
            'titre' : 'Page de connexion/inscription',
            'url_page_princ' : reverse ('appsong:page_princ')
        }
    
    if request.method == 'POST' :
        if "b_connecter" in request.POST:
            form = ConnexionForm(request.POST)
            if form.is_valid() :
                pseudo  = form.cleaned_data['pseudo']
                password = form.cleaned_data['password']
                # puis enregistrer dans la base
                log = Utilisateur.objects.filter(pseudo__iexact=pseudo)
                logg = Utilisateur.objects.get(pseudo__iexact=pseudo)
                if len(log) == 0 :
                    # Enregistrement dans la base
                
                    context['c_message'] = "Vous n'êtes pas enregister"
                else :
                    if  logg.password == request.POST['password']:
                        request.session['utilisateur'] = request.POST['pseudo']                
                        return redirect(reverse('appsong:page_princ'))
                        #context['c_message'] = 'Conneceter avec succès.'
                    else :
                        context['c_message'] = 'Erreur mot de passe.'

            else:
                form = ConnexionForm()
                context['c_form'] = form
    
    #####################################
        elif "b_enregistrement" in request.POST:
            form = EnregistrementForm(request.POST)
            if form.is_valid() :
                pseudo  = form.cleaned_data['pseudo']
                password = form.cleaned_data['password']
                password2 = form.cleaned_data['password2']
                # puis enregistrer dans la base
                liste = Utilisateur.objects.filter(pseudo__iexact=pseudo)
                if len(liste) == 0 :
                    # Enregistrement dans la base
                    if password != password2:
                        context['e_message'] = "Mot de passe différent veuillez recommencer"
                    else: 
                        nouv = Utilisateur()
                        nouv.pseudo = pseudo
                        nouv.password = password
                        nouv.save()
                        request.session['utilisateur'] = request.POST['pseudo']
                        #rejouter la condition du mdp 
                        return redirect(reverse('appsong:page_princ'))
                        #context['e_message'] = "Enregistrement effectué avec succès "
                else :
                    context['e_message'] = 'Vous avez déjà un compte.'
            else:
                form = EnregistrementForm()
                context['e_form'] = form
    return render (request, 'appsong/page_connexion.html', context)

#DONE
def gen_page_deconnexion(request) :
    context = {            
            'titre' : 'Page de deconnexion',
            'url_page_princ' : reverse ('appsong:page_princ')
        }
    if request.method == 'POST' :
        if "b_deconnexion" in request.POST:
            # Enregistrement dans la base
            del request.session['utilisateur']
            return redirect(reverse('appsong:connexion'))
    return render (request, 'appsong/page_deconnexion.html', context)
