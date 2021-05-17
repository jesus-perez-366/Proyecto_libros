from django.db import models

class categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre

class libro(models.Model):
    id = models.AutoField(primary_key = True)
    categoria = models.CharField(max_length = 100)
    titulo= models.CharField(max_length = 100)
    autor= models.CharField(max_length = 100)
    portada= models.CharField(max_length = 100)

    def __str__(self):
        return self.titulo
