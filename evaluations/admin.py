from django.contrib import admin
from .models import WeeklyEvaluation, CommonEvaluation, MatchEvaluation, DailyEvaluation, ConditioningEvaluation

# Register your models here.
admin.site.register(WeeklyEvaluation)
admin.site.register(CommonEvaluation)
admin.site.register(MatchEvaluation)
admin.site.register(DailyEvaluation)
admin.site.register(ConditioningEvaluation)
