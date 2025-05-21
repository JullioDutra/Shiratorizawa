from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confirmar-presenca/<int:match_id>/', views.confirmar_presenca, name='confirmar_presenca'),
    path('confirmar-contribuicao/', views.confirmar_contribuicao, name='confirmar_contribuicao'),
    
]
