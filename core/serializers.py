from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Projeto, Equipe

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EquipeSerializer(serializers.ModelSerializer):
    lider_nome = serializers.ReadOnlyField(source='lider.username')
    class Meta:
        model = Equipe
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    equipes = EquipeSerializer(many=True, read_only=True)
    class Meta:
        model = Projeto
        fields = '__all__'
