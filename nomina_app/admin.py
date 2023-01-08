from django.contrib import admin
from .models import Tecnico, TipoTrabajo, Semana, Dia, OtroGasto, PiezaAPagar, Venta
# Register your models here.

admin.site.register(Tecnico)
admin.site.register(TipoTrabajo)
admin.site.register(Semana)
admin.site.register(Dia)
admin.site.register(OtroGasto)
admin.site.register(PiezaAPagar)
admin.site.register(Venta)