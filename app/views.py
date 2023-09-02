from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .models import Jogo, Desenvolvedor, Cliente
from .serializers import JogoSerializer, DesenvolvedorSerializer, ClienteSerializer

class DesenvolvedorViewSet(viewsets.ModelViewSet):
    queryset = Desenvolvedor.objects.all()
    serializer_class = DesenvolvedorSerializer
    pagination_class = LimitOffsetPagination

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    pagination_class = LimitOffsetPagination

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    pagination_class = LimitOffsetPagination