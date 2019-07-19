from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.utils.translation import gettext as _
from core import models 


class UserAdmin(BaseAdmin):
    ordering   = ['id']
    list_display = ['email', 'name']

    # on update
    fieldsets = (
        (None,{'fields': ('email', 'password')}),
        (_('Personal Information'), {'fields': ('name', )}),
        (
            _('Permissions'), 
            {'fields': ('is_active', 'is_staff', 'is_superuser',)}
        ),
        (_('Importand dates'), {'fields': ('last_login',)})
    )
    #end of on updating

    #test add 
    add_fieldsets = (
        (None, 
            {
                'classes': ('wide'),
                'fields': {'email', 'password1', 'password2'},
            }
        ),
    )
    # end of add user


admin.site.register(models.User, UserAdmin)

