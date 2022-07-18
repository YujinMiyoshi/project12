from pyexpat import model
from django import forms
from .models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        exclude = ('created_at', 'updated_at',)