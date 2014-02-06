# -*- coding: utf-8 -*-
from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self): 
		return self.nombre

class Post(models.Model):
	categoria 	= models.ForeignKey(Categoria)
	titulo 		= models.CharField(max_length=200)
	contenido 	= models.TextField()
	fecha_pub 	= models.DateTimeField('fecha de publicación', auto_now_add=True)
	fecha_pub.editable=True

	def __unicode__(self): 
		return self.titulo
