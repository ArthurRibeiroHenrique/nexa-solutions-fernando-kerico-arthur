from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from .models import Chamado


class IndicadoresAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/indicadores/"  # Ajuste se o prefixo no seu urls.py raiz for diferente

    def test_indicadores_com_base_vazia(self):
        """Testa se a API retorna tudo zero quando não há chamados."""
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total"], 0)
        self.assertEqual(response.data["abertos"], 0)
        self.assertEqual(response.data["em_andamento"], 0)
        self.assertEqual(response.data["concluidos"], 0)

    def test_indicadores_com_chamados_cadastrados(self):
        """Testa se a API soma corretamente os status dos chamados."""
        # Criando dados de teste
        Chamado.objects.create(titulo="Chamado 1", status=Chamado.Status.ABERTO)
        Chamado.objects.create(titulo="Chamado 2", status=Chamado.Status.ABERTO)
        Chamado.objects.create(titulo="Chamado 3", status=Chamado.Status.EM_ANDAMENTO)
        Chamado.objects.create(titulo="Chamado 4", status=Chamado.Status.CONCLUIDO)

        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total"], 4)
        self.assertEqual(response.data["abertos"], 2)
        self.assertEqual(response.data["em_andamento"], 1)
        self.assertEqual(response.data["concluidos"], 1)
