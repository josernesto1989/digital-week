from django import forms
from nomina_app.models import Dia, Semana, Venta, OtroGasto, PiezaAPagar
from datetime import datetime

class DiaForm(forms.ModelForm):
    # client_id = forms.TextInput(attrs = {'class': 'form-control'})
    # client_secret= forms.TextInput(attrs = {'class': 'form-control'})
    # organization_id= forms.TextInput(attrs = {'class': 'form-control'})
    class Meta:
        model = Dia
        fields = ("fecha",)
        widgets = {
            'fecha': forms.DateInput(attrs = {'class':'form-control', 'type': 'date'}),
        }
        
class SemanaForm(forms.ModelForm):
    # client_id = forms.TextInput(attrs = {'class': 'form-control'})
    # client_secret= forms.TextInput(attrs = {'class': 'form-control'})
    # organization_id= forms.TextInput(attrs = {'class': 'form-control'})
    class Meta:
        model = Semana
        fields = ("nombre",)
        widgets = {
            'nombre': forms.TextInput(attrs = {'class':'form-control'}),
        }

class VentaForm(forms.ModelForm):
    # client_id = forms.TextInput(attrs = {'class': 'form-control'})
    # client_secret= forms.TextInput(attrs = {'class': 'form-control'})
    # organization_id= forms.TextInput(attrs = {'class': 'form-control'})
    class Meta:
        model = Venta
        fields = ("tipoTrabajo", "nombre","ingreso","costo",'tecnico')
        widgets = {
            # 'hora': forms.DateInput(attrs = {'class':'form-control', 'type': 'time'}),
            'tipoTrabajo': forms.Select(attrs={'class':'js-example-basic-single','style':'width:100%'}),
            'nombre': forms.TextInput(),
            'ingreso': forms.TextInput(attrs={'type':'number','style':'width:100%'}),
            'costo': forms.TextInput(attrs={'type':'number','style':'width:100%'}),
            'tecnico': forms.Select(attrs={'class':'js-example-basic-single','style':'width:100%'}),
        }
        
class OtroGastoForm(forms.ModelForm):
    # client_id = forms.TextInput(attrs = {'class': 'form-control'})
    # client_secret= forms.TextInput(attrs = {'class': 'form-control'})
    # organization_id= forms.TextInput(attrs = {'class': 'form-control'})
    class Meta:
        model = OtroGasto
        fields = ("nombre", "precio","comentarios")
        widgets = {
            'nombre': forms.TextInput(),
            'precio': forms.TextInput(attrs={'type':'number','style':'width:100%'}),
            'comentarios': forms.TextInput(attrs={'type':'text','style':'width:100%'}),
        }
        

class PiezaAPagarForm(forms.ModelForm):
    # client_id = forms.TextInput(attrs = {'class': 'form-control'})
    # client_secret= forms.TextInput(attrs = {'class': 'form-control'})
    # organization_id= forms.TextInput(attrs = {'class': 'form-control'})
    class Meta:
        model = PiezaAPagar
        fields = ("nombre", "precio","comentarios")
        widgets = {
            'nombre': forms.TextInput(),
            'precio': forms.TextInput(attrs={'type':'number','style':'width:100%'}),
            'comentarios': forms.TextInput(attrs={'type':'text','style':'width:100%'}),
        }