from django.urls import path
from .views import *


urlpatterns = [
    #URL DEPARTAMENTOS
    path('ordenes/',OrdenesView.as_view(), name='Ordenes_list'),
    path('ordenes/<int:id>', OrdenesView.as_view(), name='Ordenes_process'),  
]