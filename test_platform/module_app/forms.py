from django import forms
from models_app.models import Module


class ModuleForm(forms.ModuleForm):
    
    class Meta:
        modle = Module
        fields = ['project', 'name', 'describe']