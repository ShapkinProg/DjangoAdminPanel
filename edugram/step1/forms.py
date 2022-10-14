from django import forms
from .models import *


class AddPersonForm(forms.Form):
    name = forms.CharField(max_length=255, label='Имя')
    wiki = forms.URLField(required=False, label='Wiki')
    vk = forms.URLField(required=False, label='Vk')
    vk_subs = forms.IntegerField(required=False, label='Кол-во vk подписчиков')
    vuzs = forms.ModelMultipleChoiceField(queryset=vuz.objects.all(), widget=forms.CheckboxSelectMultiple, label='Выберите')
