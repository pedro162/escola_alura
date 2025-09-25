from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola_alura.models import Matricula, Curso, Estudante
from escola_alura.serializers import MatriculaSerializer

class SubscriptionCase(APITestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):
        self.user = User.objects.get(username="pedro")

        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.user)

        self.curso_01 = Curso.objects.get(pk=1)
        self.curso_02 = Curso.objects.get(pk=2)
        
        self.student_01 = Estudante.objects.get(pk=1)
        self.student_02 = Estudante.objects.get(pk=2)

        self.matricula_01 = Estudante.objects.get(pk=1)
        self.matricula_02 = Estudante.objects.get(pk=2)
    
    def test_makes_a_request_getting_a_subscription_list(self):
        """Makes a request getting a subscription list"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_makes_a_request_getting_only_one_subscription(self):
        """Makes a request getting only one subscription"""
        response = self.client.get(self.url+'/'+str(self.matricula_01.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        subscription_data = Matricula.objects.get(pk=self.matricula_01.pk)
        serialized_data = MatriculaSerializer(
            instance=subscription_data
        ).data

        self.assertEqual(response.data, serialized_data)

    def test_makes_a_request_creating_a_new_subscription(self):
        """Makes a request creating a new subscription"""
        data = {
            "estudante":self.student_02.pk,
            "curso":self.curso_02.pk,
            "periodo":"V"
        }
        response = self.client.post(self.url, data)
        #print(response.data)  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_makes_a_request_updating_a_subscription(self):
        """Makes a request updating a subscription"""

        data = {
            "estudante":self.student_02.pk,
            "curso":self.curso_02.pk,
            "periodo":"V"
        }

        response = self.client.put(self.url+"/"+str(self.matricula_01.pk), data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_makes_a_request_deleting_subscription(self):
        """Makes a request deleting subscription"""

        response = self.client.delete(self.url+"/"+str(self.matricula_01.pk))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)