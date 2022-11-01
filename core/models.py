from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    cidade = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

    def __str__(self):
        return self.email
        
    def __str__(self):
        return self.cidade

