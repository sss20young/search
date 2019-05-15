from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board #Board와 연결
        fields = ['title', 'body']
