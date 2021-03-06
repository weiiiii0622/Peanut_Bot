from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	
    list_display = ('user', 'status')
    list_filter = ('user', 'status')
    
    
    fieldsets = (
        (None, {'fields': ('user', 'status')}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'status'),
        }),
    )
    
    search_fields = ('user', 'status')
    ordering = ('user', 'status',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)