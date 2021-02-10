from django.contrib import admin
from . models import userData , stands , standImage , developer

# Register your models here.
admin.site.register(userData)
admin.site.register(stands)
admin.site.register(standImage)
admin.site.register(developer)

