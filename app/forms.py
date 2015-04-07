from django import forms
from app.models import *
from django.contrib.auth.models import User
from django.forms.models import formset_factory
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        exclude = ['key']

class SubscribeForm(forms.Form):
    key = forms.CharField(label='Group Key',max_length=20)

class CreateAssignmentForm(forms.ModelForm):
    due_date = forms.DateField(widget=DateInput())
    class Meta:
        model= Assignment
        exclude = ['upload_timestamp','rating','group','owner','image_count','view_count']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Images
        exclude = ['position','assignment']

AssignmentImagesFormset = formset_factory(ImageUploadForm, extra=20,max_num=20)