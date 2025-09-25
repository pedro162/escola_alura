from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola_alura.models import Curso
from escola_alura.serializers import CursoSerializer

class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            password='admin'
        )

        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.user)
        self.curso_01 = Curso.objects.create(
            codigo="ABC",
            descricao="Curso ABC",
            nivel="A"
        )

        self.curso_02 = Curso.objects.create(
            codigo="HFG",
            descricao="Curso HFG",
            nivel="A"
        )

    def test_makes_a_request_getting_a_course_list(self):
        """It makes a request getting a course list"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_makes_a_request_getting_only_one_course(self):
        """It makes a request getting only one course"""

        response = self.client.get(self.url+"/"+str(self.curso_01.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        course_data = Curso.objects.get(pk=self.curso_01.pk)
        serialized_data = CursoSerializer(instance=course_data).data
        self.assertEqual(response.data, serialized_data)

    def test_makes_a_request_creating_a_new_course(self):
        """It makes a request creating a new course"""

        data = {
            "codigo":"DSG",
            "descricao":"Curso DSG",
            "nivel":"I"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_makes_a_request_updating_a_course(self):
        """It makes a request updating a course"""

        data = {
            "codigo":"DSG",
            "descricao":"Curso DSG",
            "nivel":"I"
        }
        
        response = self.client.put(self.url+"/"+str(self.curso_01.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_makes_a_request_deleting_a_course(self):
        """It makes a request deleting a course"""

        response = self.client.delete(self.url+"/"+str(self.curso_01.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)