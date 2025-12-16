from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    STATUS_CHOICES = [
        ('planejado', 'Planejado'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    cliente = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planejado')
    data_inicio = models.DateField()
    data_fim_prevista = models.DateField()
    participantes = models.ManyToManyField(User, related_name='projetos', blank=True)

    def __str__(self):
        return self.titulo

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    projeto = models.ForeignKey(Projeto, related_name='equipes', on_delete=models.CASCADE)
    lider = models.OneToOneField(User, related_name='lider_equipe', on_delete=models.SET_NULL, null=True, blank=True)
    membros = models.ManyToManyField(User, related_name='equipes_membro', blank=True)

    def __str__(self):
        return f"{self.nome} - {self.projeto.titulo}"
