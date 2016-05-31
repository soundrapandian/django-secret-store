from django.contrib import admin

from models import SecretType, SecretStore

class SecretTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    
class SecretStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'type')
    search_fields = ('key',)
    list_filter = ('key', 'type',)
    
admin.site.register(SecretType, SecretTypeAdmin)
admin.site.register(SecretStore, SecretStoreAdmin)