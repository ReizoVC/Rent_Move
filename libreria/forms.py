from django import forms
from .models import Auto, Usuario, Empleado
from django.forms import ModelForm

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'
        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        
        widgets = {
                'password': forms.PasswordInput(),
                'FechaNacimiento': forms.DateInput(attrs={'type': 'date'}),
                'FechaExpLicencia': forms.DateInput(attrs={'type': 'date'}),
            }
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
                'Contrasena': forms.PasswordInput(),
            }
        
# class RegistroForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['username','password','Nombres','Apellidos','DNI','Email','Telefono','FechaNacimiento','Direccion','NroLicencia','FechaExpLicencia']
        
#         widgets = {
#             'password': forms.PasswordInput(),
#             'FechaNacimiento': forms.DateInput(attrs={'type': 'date'}),
#             'FechaExpLicencia': forms.DateInput(attrs={'type': 'date'}),
#         }
         
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['username','password']
        
        