from django.contrib import admin
from appsong.models import *
# Register your models here.

class ChansonAdmin(admin.ModelAdmin):
    list_display = ('id', 'groupe', 'titre', 'youtube')
    ordering = ('id',)
    filter_horizontal = ('categorie',)
    list_max_show_all = 1000

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id','nom')
    ordering = ('id',)
    list_max_show_all = 1000

class TexteAdmin(admin.ModelAdmin):
    list_display = ('chanson_id','paroles')
    ordering = ('chanson_id',)
    list_max_show_all = 1000

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('id', 'pseudo','password')
    ordering = ('id',)
    list_max_show_all = 1000

admin.site.register(Chanson, ChansonAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Texte, TexteAdmin)
admin.site.register(Utilisateur, UtilisateurAdmin)