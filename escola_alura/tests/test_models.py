from django.test import TestCase
from escola_alura.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    # def test_fail(self):
    #     self.fail('Teste falhou')

    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome='Teste modelo',
            email='teste@gmail.com',
            cpf='61224450370',
            data_nascimento='2023-09-09',
            celular='98 99999-9999'
        )

        self.curso = Curso.objects.create(
            codigo='TST',
            descricao='Teste',
            nivel="A"
        )

        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo='N'
        )

    def test_check_student_attributes(self):
        """Verify student model attributes"""
        self.assertEqual(self.estudante.nome, 'Teste modelo')
        self.assertEqual(self.estudante.email, 'teste@gmail.com')
        self.assertEqual(self.estudante.cpf, '61224450370')
        self.assertEqual(self.estudante.data_nascimento, '2023-09-09')
        self.assertEqual(self.estudante.celular, '98 99999-9999')
    
    def test_check_curse_attributes(self):
        """Verify curse model attributes"""
        self.assertEqual(self.curso.codigo, 'TST')
        self.assertEqual(self.curso.descricao, 'Teste')
        self.assertEqual(self.curso.nivel, 'A')
    
    def test_check_enroll_curse(self):
        """Verify enroll student to curse"""
        self.assertEqual(self.matricula.curso, self.curso)
        self.assertEqual(self.matricula.estudante, self.estudante)
        self.assertEqual(self.matricula.periodo, 'N')