from django.contrib import admin

# Register your models here.
from Message.models import DirectMessage

admin.site.register(DirectMessage)
