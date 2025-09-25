from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola_alura.models import Estudante
from escola_alura.serializers import EstudanteSerializer

class StudentTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            password='admin'
        )

        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.user)
        self.student_01 = Estudante.objects.create(
            nome='Student 01',
            email='estudent_01@gmail.com',
            cpf='35573671006',
            data_nascimento='2023-09-09',
            celular='98 99999-9999'
        )

        self.student_02 = Estudante.objects.create(
            nome='Student 02',
            email='estudent_02@gmail.com',
            cpf='70287704009',
            data_nascimento='2023-09-09',
            celular='98 99999-9999'
        )

    def test_makes_a_request_getting_a_student_list(self):
        """Makes a request getting a student list"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_makes_a_request_getting_only_one_student(self):
        """Makes a request getting only one student"""
        response = self.client.get(self.url+'/'+str(self.student_01.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        student_data = Estudante.objects.get(pk=self.student_01.pk)
        serialized_data = EstudanteSerializer(
            instance=student_data
        ).data

        self.assertEqual(response.data, serialized_data)

    def test_makes_a_request_creating_a_new_student(self):
        """Makes a request creating a new student"""
        data = {
            'nome':'Student',
            'email':'estudent_03@gmail.com',
            'cpf':'45551641058',
            'data_nascimento':'2002-06-24',
            'celular':'11 95823-9311'
        }
        response = self.client.post(self.url, data)
        #print(response.data)  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_makes_a_request_updating_a_student(self):
        """Makes a request updating a student"""

        data = {
            'nome':'Student',
            'email':'estudent_05@gmail.com',
            'cpf':'88777591003',
            'data_nascimento':'2023-09-09',
            'celular':'98 99999-9999'
        }

        response = self.client.put(self.url+"/"+str(self.student_01.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_makes_a_request_deleting_student(self):
        """Makes a request deleting student"""

        response = self.client.delete(self.url+"/"+str(self.student_01.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)