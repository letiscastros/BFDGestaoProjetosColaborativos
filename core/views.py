from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Projeto, Equipe
from .serializers import ProjetoSerializer, EquipeSerializer, UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='visao-geral')
    def visao_geral(self, request, pk=None):
        user = self.get_object()
        data = { "usuario": UserSerializer(user).data, "projetos": [] }
        for proj in user.projetos.all():
            equipes = proj.equipes.filter(membros=user)
            p_data = ProjetoSerializer(proj).data
            p_data['equipes'] = EquipeSerializer(equipes, many=True).data
            data["projetos"].append(p_data)
        return Response(data)

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def participantes(self, request, pk=None):
        try:
            user = User.objects.get(id=request.data.get('user_id'))
            self.get_object().participantes.add(user)
            return Response({'status': 'ok'})
        except: return Response({'error': 'Erro'}, status=400)

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['put'], url_path='definir-lider')
    def definir_lider(self, request, pk=None):
        try:
            user = User.objects.get(id=request.data.get('user_id'))
            equipe = self.get_object()
            if hasattr(user, 'lider_equipe') and user.lider_equipe != equipe:
                return Response({'error': 'Ja e lider'}, status=400)
            equipe.lider = user
            equipe.save()
            return Response({'status': 'ok'})
        except: return Response({'error': 'Erro'}, status=400)
