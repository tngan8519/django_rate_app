from django import forms
from django.contrib.auth import get_user_model

from .models import Individual,Rating

User = get_user_model()

class IndividualCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"enter name"}))
    image=forms.ImageField(widget=forms.FileInput(attrs={ "class":"form-control-file","id":"pic","name":"myImage"}))
    description = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"enter description"}))

    class Meta:
        model = Individual
        fields = ['name','image','description']

class RatingCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RatingCreateForm, self).__init__(*args, **kwargs)
        self.fields['rating'].required = False
        self.fields['text'].required = False

    MY_CHOICES=[('5','5'),('4','4'),('3','3'),('2','2'),('1','1')]
    # rating = forms.ChoiceField(widget=forms.RadioSelect(choices=MY_CHOICES))
    rating = forms.ChoiceField(choices = MY_CHOICES, widget=forms.RadioSelect)
    text = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"enter your review","rows":"7" ,"style":"resize: none"}))

    class Meta:
        model = Rating
        fields = ['rating','text'] 

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"type name ..."}))
    reset = forms.CharField()