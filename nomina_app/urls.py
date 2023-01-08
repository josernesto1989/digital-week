"""digitalWeek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from nomina_app import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mainView, name ='main'),
    path('semana/abrir',views.createSemana, name ='semana_abrir'),
    path('semana/crear',views.createNewSemana, name ='semana_crear'),
    path('dia/abrir',views.createDia, name ='dia_abrir'),
    path('dia/cerrar',views.colseDay, name ='dia_cerrar'),
    path('dia/crear',views.createNewDia, name ='dia_crear'),
    path('venta/crear',views.createNewVenta, name ='venta_crear'),
    path('otro-gasto/crear',views.createNewGasto, name ='otroGasto_crear'),
    path('pieza-a-pagar/crear',views.createNewPiezaAPagar, name ='piezaAPagar_crear'),
    path('template',views.template, name ='template'),
    path('excel/export',views.exportToExcel, name ='toExcel'),
    
    
]
