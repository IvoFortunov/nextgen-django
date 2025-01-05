from django.contrib import admin
from .models import Profile, Messages, Presentation, PlayerOTW

# Register your models here.
admin.site.register(Profile)
admin.site.register(Messages)
admin.site.register(Presentation)
admin.site.register(PlayerOTW)
