# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  16:01
@author: xuanyue
@file: froms.py
"""
from django import forms
from project_app.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']