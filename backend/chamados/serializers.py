from rest_framework import serializers

from .models import Chamado


class ChamadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamado
        fields = [  # noqa: RUF012
            "id",
            "titulo",
            "descricao",
            "status",
            "criado_em",
            "atualizado_em",
        ]
        extra_kwargs = {  # noqa: RUF012
            "titulo": {
                "required": True,
                "allow_blank": False,
            },
        }
        read_only_fields = [  # noqa: RUF012
            "id",
            "criado_em",
            "atualizado_em",
        ]