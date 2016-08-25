# -*- coding: utf-8 -*-
from django.db import models

class Entrada(models.Model):
    class Meta:
        verbose_name = "Mi Entrada"
        verbose_name_plural = "Todas mis entradas"
        ordering=['-fecha']

    titulo = models.CharField(u'Titulo', max_length=100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    resumen= models.CharField(u'Resumen',max_length=512)
    contenido = models.TextField(u'Contenido')
    

    def __str__(self):
        return self.titulo


    
