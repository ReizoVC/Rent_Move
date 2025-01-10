from django.contrib import admin
from.models import Auto
from.models import Usuario
from.models import Empleado


admin.site.register(Auto)
admin.site.register(Usuario)
admin.site.register(Empleado)


# Register your models here.

#python manage.py createsuperuser