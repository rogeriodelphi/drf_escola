from rest_framework import generics

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursosAPIView(generics.ListCreateAPIView):
    """Listar ou criar um curso"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Atualiza ou deletar um curso"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer



class AvaliacoesAPIView(generics.ListCreateAPIView):
    """Listar ou criar uma avaliação"""
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Atualiza ou deletar uma Avaliação"""
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
