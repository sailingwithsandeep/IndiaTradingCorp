from django import forms
from .models import *


class EmailForm(forms.ModelForm):

    class Meta:
        model = Email_Newsletter
        fields = ('emailAddress',)
        lables = {'emailAddress': 'Email Address', }

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
