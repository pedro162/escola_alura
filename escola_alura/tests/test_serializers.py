from django.test import TestCase
from escola_alura.models import Estudante, Curso, Matricula
from escola_alura.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class SerializerStudentTest(TestCase):
    def setUp(self):
        self.student = Estudante(
            nome='Teste modelo',
            email='teste@gmail.com',
            cpf='61224450370',
            data_nascimento='2023-09-09',
            celular='98 99999-9999'
        )
        
        self.student_fields = ['id', 'nome','email', 'cpf','data_nascimento', 'celular']
        self.student_serializer = EstudanteSerializer(instance=self.student)

    def test_verify_student_data_serializer(self):
        """Verify serialized fields"""

        data = self.student_serializer.data
        self.assertEqual(set(data.keys()), set(self.student_fields))

    def test_verify_student_content_serializer(self):
        """Verify serialized content"""

        data = self.student_serializer.data
        self.assertEqual(data['nome'], self.student.nome)
        self.assertEqual(data['email'], self.student.email)
        self.assertEqual(data['cpf'], self.student.cpf)
        self.assertEqual(data['data_nascimento'], self.student.data_nascimento)
        self.assertEqual(data['celular'], self.student.celular)

class SerializerCourseTest(TestCase):
    def setUp(self):
        self.course = Curso(
            codigo='TST',
            descricao='Teste',
            nivel="A"
        )
        
        self.course_fields = ['id', 'codigo','descricao', 'nivel']
        self.course_serializer = CursoSerializer(instance=self.course)

    def test_verify_course_data_serializer(self):
        """Verify serialized curse fields"""

        data = self.course_serializer.data
        self.assertEqual(set(data.keys()), set(self.course_fields))

    def test_verify_course_content_serializer(self):
        """Verify serialized curse content"""

        data = self.course_serializer.data
        self.assertEqual(data['codigo'], self.course.codigo)
        self.assertEqual(data['descricao'], self.course.descricao)
        self.assertEqual(data['nivel'], self.course.nivel)

class SerializerSubscriptionTest(TestCase):
    def setUp(self):
        self.course = Curso(
            codigo='TST',
            descricao='Teste',
            nivel="A"
        )

        self.student = Estudante(
            nome='Teste modelo',
            email='teste@gmail.com',
            cpf='61224450370',
            data_nascimento='2023-09-09',
            celular='98 99999-9999'
        )
        
        self.subscription = Matricula(
            estudante=self.student,
            curso=self.course,
            periodo='N'
        )

        self.subscription_fields=  ['id', 'estudante','curso', 'periodo']
        self.subscription_serializer = MatriculaSerializer(instance=self.subscription)
    
    def test_verify_subscription_data_serializer(self):
        """verify the serializer subscription field"""

        data = self.subscription_serializer.data
        self.assertEqual(set(data.keys()), set(self.subscription_fields))

    def test_verify_subscription_content_serializer(self):
        """Verify serialized subscription content"""

        data = self.subscription_serializer.data
        self.assertEqual(data['estudante'], self.subscription.estudante.pk)
        self.assertEqual(data['curso'], self.subscription.curso.pk)
        self.assertEqual(data['periodo'], self.subscription.periodo)