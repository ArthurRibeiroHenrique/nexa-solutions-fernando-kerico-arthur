from rest_framework import generics

from .models import Chamado
from .serializers import ChamadoSerializer


class ChamadoListCreateView(generics.ListCreateAPIView):
    """
    Lista e cria chamados.

    Limitações intencionais:
    - Não filtra chamados por status.
    - Não oferece indicadores.
    - Não há tratamento adicional para parâmetros inválidos.
    """

    queryset = Chamado.objects.all().order_by("-criado_em")
    serializer_class = ChamadoSerializer


class ChamadoDetailView(generics.RetrieveUpdateAPIView):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer
    
from django.db.models import Count, Q
from rest_framework.response import Response
from rest_framework.views import APIView

# ... (mantenha suas views atuais aqui em cima) ...

class IndicadoresView(APIView):
    """
    Retorna indicadores resumidos sobre o volume de chamados.
    """
    def get(self, request):
        # Faz a contagem em uma única query no banco de dados
        indicadores = Chamado.objects.aggregate(
            total=Count("id"),
            abertos=Count("id", filter=Q(status=Chamado.Status.ABERTO)),
            em_andamento=Count("id", filter=Q(status=Chamado.Status.EM_ANDAMENTO)),
            concluidos=Count("id", filter=Q(status=Chamado.Status.CONCLUIDO)),
        )
        
        return Response(indicadores)