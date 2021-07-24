from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . import models
from quiz import models as QMODEL






class StudentUserForm(forms.ModelForm):


    
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput(),
        'username': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        users_available = models.UserAvailable.objects.all()
        list_users = []
        for user in users_available:
            list_users.append(user.name)
        print('List username', list_users)
        if username not in list_users:
            raise ValidationError('You need to entrer a valid username')
        return username

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['address','mobile','profile_pic']
    
