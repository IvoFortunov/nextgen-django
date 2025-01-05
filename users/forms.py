from django.forms import ModelForm
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import AbstractBaseUser
from .models import Profile, User, Messages, PlayerOTW

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        # labels = {
        #     'first_name': 'Име',
        #     'last_name': 'Фамилия',
        #     'first_name': 'Имейл',
            
        # }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'linked_email', 'username', 'location', 'intro', 'bio', 'profile_image', 'hand', 'backhand', 'date_of_birth',
                   'social_facebook', 'social_instagram' ]
        labels = {
            'name':'Име', 
            'email':'Имейл', 
            'linked_email':'Имейл родител', 
            'username':'Потребителско име', 
            'location':'Локация', 
            'intro':'Въведение', 
            'bio':'За мен', 
            'profile_image':'Профилна снимка', 
            'hand':'Играеща ръка', 
            'backhand':'Бекхенд', 
            'date_of_birth':'Дата на раждане (YYYY-MM-DD)',
            'social_facebook':'Facebook', 
            'social_instagram':'Instagram'}

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = AbstractBaseUser

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['subject', 'body']
        labels = {
            'subject':'Тема', 
            'body':'Съобщение', 
            }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class PlayerOTWForm(ModelForm):
    class Meta:
        model = PlayerOTW
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(PlayerOTWForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})