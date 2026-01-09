from django.contrib import admin
from .models import Projeto, Equipe

# Configuração para o Projeto
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'status', 'data_inicio')
    list_filter = ('status',)
    search_fields = ('titulo', 'cliente')

# Configuração simples para a Equipe
admin.site.register(Equipe)
