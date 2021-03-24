from django import forms
from .models import *


class EmailForm(forms.ModelForm):

    class Meta:
        model = Email_Newsletter
        fields = ('emailAddress',)
        lables = {'emailAddress': 'Email Address', }

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        emailAddress = self.cleaned_data.get('emailAddress')
        if emailAddress and Email_Newsletter.objects.filter(emailAddress=emailAddress).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return emailAddress

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ('name','contactEmail','message')
        labels = {'name': 'Name','contactEmail': 'Email Address','message': 'Message'}
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)