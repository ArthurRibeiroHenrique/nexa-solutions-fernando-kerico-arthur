from rest_framework.test import APITestCase
from rest_framework import status
from .models import Chamado

class ChamadosAPITests(APITestCase):
    def setUp(self):
        # Criando chamados de teste antes de cada função rodar
        Chamado.objects.create(titulo="Internet caindo", status="ABERTO")
        Chamado.objects.create(titulo="Teclado quebrado", status="CONCLUIDO")

    # --- TESTES DE CRIAÇÃO (INC-01) ---
    def test_criacao_valida(self):
        dados = {"titulo": "Mouse parou de funcionar", "descricao": "Urgente"}
        response = self.client.post('/api/chamados/', dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Chamado.objects.count(), 3)

    def test_criacao_sem_titulo(self):
        dados = {"descricao": "Faltou o título"}
        response = self.client.post('/api/chamados/', dados)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # --- TESTES DE FILTRO (INC-02) ---
    def test_filtro_status_valido(self):
        response = self.client.get('/api/chamados/?status=ABERTO')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados = response.data.get('results', response.data) if isinstance(response.data, dict) else response.data
        self.assertEqual(len(dados), 1)
        self.assertEqual(dados[0]['titulo'], "Internet caindo")

    def test_filtro_status_invalido(self):
        response = self.client.get('/api/chamados/?status=BANANA')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("erro", response.data)

    # --- TESTES DE INDICADORES (INC-06) ---
    def test_indicadores_retorno(self):
        response = self.client.get('/api/indicadores/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Validando as chaves exatas que o seu colega criou:
        self.assertIn("abertos", response.data)
        self.assertEqual(response.data["abertos"], 1)
        self.assertEqual(response.data["concluidos"], 1)
        self.assertEqual(response.data["total"], 2)