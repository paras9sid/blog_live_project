from django.contrib import admin
from .models import About


# Register your models here.

# only 1 about us allowed in admin panel
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self,request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False
    
admin.site.register(About,AboutAdmin)