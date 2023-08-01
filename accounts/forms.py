from django.forms import ModelForm
from .models import newUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model=newUser
        fields=['username','email','phone_number','fav_books','user_profile_image']

    def clean(self):
        data=self.cleaned_data
        username=data.get('username')
        dp=data.get('user_profile_image')
        print(dp)
        qs=newUser.objects.filter(username__icontains=username)
        if(qs.exists()):
            self.add_error("username",f'"{username}" already exists. Please choose another one.')
        return data
    
class ProfileUpdateForm(ModelForm):
    class Meta:
        model=newUser
        fields=['username','email','phone_number','fav_books','user_profile_image']