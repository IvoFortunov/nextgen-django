from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import WeeklyEvaluation, CommonEvaluation, MatchEvaluation, DailyEvaluation, ConditioningEvaluation


class EditWeeklyForm(ModelForm):
    class Meta:
        model = WeeklyEvaluation
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(EditWeeklyForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 


class EditCommonForm(ModelForm):
    class Meta:
        model = CommonEvaluation
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(EditCommonForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 


class EditMatchForm(ModelForm):
    class Meta:
        model = MatchEvaluation
        fields = '__all__'
        labels = {
            'player':'Играч', 
            'matchtype':'Тип мач', 
            'tournament':'Турнир', 
            'round':'Кръг', 
            'opponent':'Противник', 
            'winloose':'Победа/загуба', 
            'result':'Резултат', 
            'comments':'Коментар', 
            'coachVisible':'Видим за треньора'}
        
    def __init__(self, *args, **kwargs):
        super(EditMatchForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 

class EditDailyForm(ModelForm):
    class Meta:
        model = DailyEvaluation
        fields = '__all__'
        labels = {
            'player':'Играч', 
            'coach':'Треньор', 
            'date':'Дата', 
            'mark':'Оценка',
            'practicetype':'Тип тренировка', 
            'comments':'Коментар', 
            'coachVisible':'Видим за треньора'}
        
    def __init__(self, *args, **kwargs):
        super(EditDailyForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 


class EditConditioningForm(ModelForm):
    class Meta:
        model = ConditioningEvaluation
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(EditConditioningForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 

