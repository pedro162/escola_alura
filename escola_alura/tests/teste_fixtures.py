from django.test import TestCase
from escola_alura.models import Estudante, Curso

class FixTuresTetCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_loading_fixtures(self):
        """It tests the loading of fixtures"""

        student = Estudante.objects.get(cpf="11111111112")
        curse = Curso.objects.get(pk=1)
        self.assertEqual(student.celular, "98984257623")
        self.assertEqual(curse.codigo, "JS")