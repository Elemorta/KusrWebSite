from django import forms
from .models import *


class Application(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Town'].empty_label = 'Город не выбран'
        self.fields['Street'].empty_label = 'Улица не выбрана'
        self.fields['Bundle'].empty_label = 'Не выбран пакет'

    class Meta:
        model = Application
        fields = ['Name_Client', 'Phone_Number', 'Street', 'Town', 'House', 'Entrance', 'Floor', 'Flat', 'Bundle']
