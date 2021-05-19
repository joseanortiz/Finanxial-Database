from django.contrib import admin
from .models import Client
from .models import File
from .models import ClientGroup

admin.site.register(Client)
admin.site.register(File)
admin.site.register(ClientGroup)
