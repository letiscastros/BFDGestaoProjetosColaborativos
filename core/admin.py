from django.contrib import admin
from .models import Projeto, Equipe
admin.site.register(Projeto)
admin.site.register(Equipe)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'status', 'data_inicio')
    list_filter = ('status',)
    search_fields = ('titulo', 'cliente')
