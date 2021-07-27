from django.contrib import admin
from .models import Client
from .models import File
from .models import ClientGroup
from .models import Manager
from .models import Partner
from .models import Industrie
from .models import Contact


admin.site.register(Client)
admin.site.register(File)
admin.site.register(ClientGroup)
admin.site.register(Manager)
admin.site.register(Partner)
admin.site.register(Industrie)
admin.site.register(Contact)
