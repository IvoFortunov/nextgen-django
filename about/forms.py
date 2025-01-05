from django.forms import ModelForm
from .models import About

class EditAboutForm(ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        labels = {
            'description':'Описание', 
            'address':'Адрес', 
            'mobile':'Телефон', 
            'email':'Имейл', 
            'social_facebook':'Facebook', 
            'social_instagram':'Instagram'}

        
    def __init__(self, *args, **kwargs):
        super(EditAboutForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 