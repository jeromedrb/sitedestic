from django.contrib import admin
from .models import Message, Usersinfo, Solutions
from .models import demandesolution
# Register your models here.



admin.site.register(Message)
admin.site.register(Usersinfo)
admin.site.register(Solutions)
admin.site.register(demandesolution)
