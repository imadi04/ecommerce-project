from django import forms
from django.contrib.auth.models import User
from cart.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Last Name'}))


    class Meta():
        model=User
        fields=('first_name','last_name','username','email','password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



class UserProfileInfoForm(forms.ModelForm):
    place = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Place'}))
    class Meta():
        model=UserProfileInfo
        fields=('place',)

    def __init__(self, *args, **kwargs):
        super(UserProfileInfoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
