from django import forms
from .models import Pokemon, Trainer

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        #fields = ['name', 'type', 'weight', 'trainer', 'picture']
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
        labels = {
            'name': 'Nombre',
            'type': 'Tipo',
            'weight': 'Peso',
            'height': 'Altura',
            'trainer': 'Entrenador',
            'picture': 'Imagen'
        }
        
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'level': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'birth_date': 'Fecha de Nacimiento',
            'level': 'Nivel',
            'picture': 'Imagen'
        }