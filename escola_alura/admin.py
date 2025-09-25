from django.contrib import admin
from escola_alura.models import Estudante,Curso,Matricula

class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'data_nascimento', 'celular',)
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome','cpf',)
    ordering = ('nome',)

admin.site.register(Estudante, Estudantes)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao',)
    list_display_links = ('id', 'codigo', 'descricao',)
    search_fields = ('codigo',)

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'curso', 'estudante', 'periodo',)
    list_display_links = ('id', 'curso', 'estudante',)
    search_fields = ('id', 'curso', 'estudante',)

admin.site.register(Matricula, Matriculas)
#admin@gmai.com#pedro#123456