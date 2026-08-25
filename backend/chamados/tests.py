from rest_framework.test import APITestCase
from rest_framework import status
from .models import Chamado

class ChamadoFiltroTests(APITestCase):
    def setUp(self):
        # Cria dois chamados de mentira no banco de testes
        Chamado.objects.create(titulo="Internet caindo", status="ABERTO")
        Chamado.objects.create(titulo="Teclado quebrado", status="CONCLUIDO")

    def test_filtro_status_valido(self):
        # Testa se a busca por ABERTO traz apenas 1 chamado
        response = self.client.get('/api/chamados/?status=ABERTO')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # O Django REST retorna paginação ou lista direta
        dados = response.data.get('results', response.data) if isinstance(response.data, dict) else response.data
        self.assertEqual(len(dados), 1)
        self.assertEqual(dados[0]['titulo'], "Internet caindo")

    def test_filtro_status_invalido(self):
        # Testa se a busca por BANANA retorna Erro 400
        response = self.client.get('/api/chamados/?status=BANANA')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("erro", response.data)