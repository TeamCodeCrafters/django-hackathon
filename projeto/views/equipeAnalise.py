# views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import EquipeAnalise
from ..serializers import EquipeAnaliseSerializer

class EquipeAnaliseViewSet(viewsets.ModelViewSet):
    queryset = EquipeAnalise.objects.all()
    serializer_class = EquipeAnaliseSerializer

    @action(detail=True, methods=['post', 'get'])
    def aceitar_equipe(self, request, pk=None):
        equipe_analise = self.get_object()

        # Verificar se o status é "aceita" antes de mover
        if equipe_analise.status == 'aceita':
            equipe_analise.mover_para_equipe()  # Mover para a model Equipe

            serializer = self.get_serializer(equipe_analise)
            return Response(serializer.data)
        else:
            return Response({'detail': 'A equipe não está marcada como aceita.'}, status=400)

    @action(detail=True, methods=['post'])
    def rejeitar_equipe(self, request, pk=None):
        equipe_analise = self.get_object()
        equipe_analise.status = 'rejeitada'
        equipe_analise.save()
        serializer = self.get_serializer(equipe_analise)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        equipes_pendentes = self.queryset.filter(status='pendente')
        serializer = self.get_serializer(equipes_pendentes, many=True)
        return Response(serializer.data)