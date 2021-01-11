from django import forms

from .models import User

class UserCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(UserCreateForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['admin_code'].required = False

    admin_code = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username','password','admin_code']

    def get_code(self):
       return self.admin_code