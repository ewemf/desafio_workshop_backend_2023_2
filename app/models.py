from django.db import models

class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=100)
    sede = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    titulo = models.CharField(max_length=100)
    desenvolvedor = models.ForeignKey(Desenvolvedor, on_delete=models.CASCADE)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.titulo

class Cliente(models.Model):
    nome = models.CharField(max_length=100);
    endereco = models.CharField(max_length=120);
    telefone = models.CharField(max_length=12);
    
    def __str__(self):
        return self.nome;