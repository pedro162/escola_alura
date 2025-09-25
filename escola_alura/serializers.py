from rest_framework import serializers
from escola_alura.models import Estudante,Curso,Matricula,Imagem
from escola_alura.validators import cpf_invalido, nome_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome','email', 'cpf','data_nascimento', 'celular']

    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF é inválido!'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular':'O celular precisa seguir o modelo 99 99999-9999'})
        
        return dados

    def validate_cpf(self, cpf:str)->str:
        if cpf_invalido(cpf):
            raise serializers.ValidationError('O CPF é inválido!')
        
        return cpf
    
    def validate_nome(self, nome:str):
        if nome_invalido(nome):
            raise serializers.ValidationError('O nome só pode ter letras')
        
        return nome
    
    def validate_celular(self, celular:str)->str:
        if celular_invalido(celular):
            raise serializers.ValidationError('O celular precisa seguir o modelo 99 99999-9999')
        
        return celular

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculaCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome','email', 'celular']

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imagem
        fields = '__all__'