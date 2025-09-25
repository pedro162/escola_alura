from escola_alura.models import Estudante, Curso, Matricula, Imagem
from escola_alura.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaCursoSerializer, ListaMatriculasEstudanteSerializer, EstudanteSerializerV2, ImageSerializer
from rest_framework import viewsets, generics, filters
#from rest_framework.authentication import BasicAuthentication
#from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by('nome')
    #serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome', 'cpf', 'data_nascimento', 'id']
    search_fields = ['nome', 'cpf', 'data_nascimento', 'id']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer
class CursoViewSet(viewsets.ModelViewSet):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = Curso.objects.all().order_by('descricao')
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['codigo', 'descricao', 'nivel']

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by('curso__descricao')
    serializer_class = MatriculaSerializer
    http_method_names=["get", "post"]

class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('curso__descricao')
    
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('curso__descricao')
    
    serializer_class = ListaMatriculaCursoSerializer

class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all().order_by('pk')
    serializer_class = ImageSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['pk', 'descricao']

#pip freeze > requirements.txt