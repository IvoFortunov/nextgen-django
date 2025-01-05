from django import forms
from django.forms import ModelForm
from .models import Program, ProgramImage

class EditProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        labels = {
            'name':'Заглавие', 
            'image':'Заглавна снимка', 
            'description':'Описание'}
        
    def __init__(self, *args, **kwargs):
        super(EditProgramForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True
    required = False

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
    
class ProgramImageForm(ModelForm):
    # images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'input', 'allow_multiple_selected':True}))
    images = MultipleFileField()
    class Meta:
        model = ProgramImage
        fields = ['images']
        labels = {
            'images':'Галерия'}