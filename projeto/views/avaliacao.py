from rest_framework.viewsets import ModelViewSet
from ..models import Avaliacao
from ..serializers import AvaliacaoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
