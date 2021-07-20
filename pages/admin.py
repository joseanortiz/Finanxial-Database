from django.contrib import admin
from .models import Client
from .models import File
from .models import ClientGroup
from .models import Employee
from .models import Industrie
from .models import Contact


admin.site.register(Client)
admin.site.register(File)
admin.site.register(ClientGroup)
admin.site.register(Employee)
admin.site.register(Industrie)
admin.site.register(Contact)
