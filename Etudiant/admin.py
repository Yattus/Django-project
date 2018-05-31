from django.contrib import admin
from django.utils.text import Truncator
from .models import User, Cour, Exercise, Serie
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display= ('pseaudo', 'apercu_email')
    list_filter= ('pseaudo',)
    ordering= ('date',)
    date_hierarchy= 'date'
    search_fields= ('date', 'pseaudo')

    def apercu_email(self, user):
        """ retourne les 20 premier char de l'Email"""

        return Truncator(user.email).chars(20, truncate= '...')

    apercu_email.short_description= 'Email'

admin.site.register(User, UserAdmin)
admin.site.register(Cour)
admin.site.register(Exercise)
admin.site.register(Serie)