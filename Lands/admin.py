from django.contrib import admin
from . models import userData , stands , standImage , developer, feed

# Register your models here.
admin.site.register(userData)
admin.site.register(stands)
admin.site.register(standImage)
admin.site.register(developer)
admin.site.register(feed)

