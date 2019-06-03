from django.urls import path
from . import views
from appsong.views import *
from django.urls import re_path
from django.conf.urls import url

app_name = 'appsong'
urlpatterns = [
    #path(r'^search/$', views.search, name='search'),
    path('princ/', views.gen_page_principale, name='page_princ'),
    path('chanson/<int:chanson_id>/',views.gen_page_chanson,name='page_chanson'),
    path('chanson/nouv/',views.gen_nouv_chanson, name='nouv_chanson'),
    path('chanson/<int:chanson_id>/modif/', views.gen_modif_chanson, name='modif_chanson'),
    path('categorie/', views.gen_page_cate, name = 'gerer_cate'),
    path('categorie/delete/<int:cate_id>', views.delete, name = 'delete'),
    #path('categorie/modifier/<int:cate_id>', views.modifier, name = 'modifier'),
    path('categorie/add/', views.gen_add_cate, name='add_cate'),
    path('chanson/<int:chanson_id>/cate_of_chanson/', views.gen_cate_of_chanson, name='cate_of_chanson'),
    path('',views.gen_page_principale, name='page_princ_empty'),
    path('connexion/', views.gen_page_connexion, name= 'connexion'),
     path('deconnexion/', views.gen_page_deconnexion, name= 'deconnexion'),
]