from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .models import Chamado
from .serializers import ChamadoSerializer


class ChamadoListCreateView(generics.ListCreateAPIView):
    """
    Lista e cria chamados.
    Permite filtrar por status através de query params.
    """
    serializer_class = ChamadoSerializer

    def get_queryset(self):
        queryset = Chamado.objects.all().order_by("-criado_em")
        status_param = self.request.query_params.get("status")

        if status_param:
            status_validos = [escolha[0] for escolha in Chamado.Status.choices]
            if status_param not in status_validos:
                raise ValidationError({
                    "erro": f"Status inválido. Escolhas permitidas: {', '.join(status_validos)}."
                })
            queryset = queryset.filter(status=status_param)

        return queryset


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