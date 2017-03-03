# -*- coding: utf-8 -*- 
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=5)
    email = forms.EmailField(min_length=5)
    message = forms.CharField(min_length=10)