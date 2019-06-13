from django.contrib import admin

# Register your models here.
from .models import News
from .models import Registration
from .models import Hobby
from .models import Gender
# from .models import InheritRegistration

admin.site.register(News)
admin.site.register(Registration)
admin.site.register(Hobby)
admin.site.register(Gender)

# admin.site.register(InheritRegistration)