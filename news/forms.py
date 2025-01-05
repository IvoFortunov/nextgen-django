from django.forms import ModelForm
from .models import News

class EditNewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        labels = {
            'author':'Автор', 
            'title':'Заглавие', 
            'image':'Снимка',
            'body': 'Описание'}
        
    def __init__(self, *args, **kwargs):
        super(EditNewsForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 