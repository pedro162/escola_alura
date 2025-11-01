from escola_alura.models import Estudante, Curso, Matricula, Imagem
from escola_alura.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaCursoSerializer, ListaMatriculasEstudanteSerializer, EstudanteSerializerV2, ImageSerializer
from rest_framework import viewsets, generics, filters
#from rest_framework.authentication import BasicAuthentication
#from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from escola_alura.throttler import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Endpoint para gerenciar estudantes.
    Métodos Permitidos:
    - GET: Retorna uma lista de estudantes.
    - POST: Cria um novo estudante.
    - PUT: Atualiza um estudante existente.
    - DELETE: Remove um estudante existente.
    Versão da API:
    - v1: Retorna dados no formato padrão.
    - v2: Retorna dados com o campo 'idade' adicional.
    """

    queryset = Estudante.objects.all().order_by('id')
    #serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome', 'cpf', 'data_nascimento', 'id']
    search_fields = ['nome', 'cpf', 'data_nascimento', 'id']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Endpoint para gerenciar cursos.
    Métodos Permitidos:
    - GET: Retorna uma lista de cursos.
    - POST: Cria um novo curso.
    - PUT: Atualiza um curso existente.
    - DELETE: Remove um curso existente.
    """
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['codigo', 'descricao', 'nivel']
    permission_classes = [IsAuthenticatedOrReadOnly]

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Endpoint para gerenciar matrículas de estudantes em cursos.
    
    Métodos Permitidos:
    - GET: Retorna uma lista de matrículas.
    - POST: Cria uma nova matrícula.

    Throttling:
    - UserRateThrottle: Limita a taxa de requisições por usuário autenticado.
    - MatriculaAnonRateThrottle: Limita a taxa de requisições por usuários anônimos.
    """

    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    http_method_names=["get", "post"]
    throttle_classes= [UserRateThrottle,MatriculaAnonRateThrottle]

class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matricula por id de Estudante
    Parâmetros:
    - pk (int): O identifificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
    
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matricula por id de Curso
    Parâmetros:
    - pk (int): O identifificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
    
    serializer_class = ListaMatriculaCursoSerializer

class ImagemViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Endpoint para gerenciar imagens.
    Métodos Permitidos:
    - GET: Retorna uma lista de imagens.
    - POST: Cria uma nova imagem.
    - PUT: Atualiza uma imagem existente.
    - DELETE: Remove uma imagem existente.
    """
    queryset = Imagem.objects.all().order_by('pk')
    serializer_class = ImageSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['pk', 'descricao']

#pip freeze > requirements.txt