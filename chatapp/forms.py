from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=50, required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=50, required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'