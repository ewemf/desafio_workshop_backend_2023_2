from django.contrib import admin
from .models import Jogo, Cliente, Desenvolvedor
# username: admin 
# password: admin

class JogosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'desenvolvedor', 'genero', 'plataforma', 'preco')

admin.site.register(Jogo, JogosAdmin)


class DesenvolvedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sede')

admin.site.register(Desenvolvedor, DesenvolvedorAdmin)
    

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(Cliente, ClienteAdmin)