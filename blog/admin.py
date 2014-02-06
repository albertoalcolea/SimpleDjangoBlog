# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Categoria, Post


class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		('Categoría',	{'fields': ['categoria']}),
		('Post',		{'fields': ['titulo', 'contenido']}),
		('Fecha',		{'fields': ['fecha_pub'], 'classes': ['collapse']}),
	]
	list_display = ('titulo', 'categoria', 'fecha_pub')
	list_filter = ['fecha_pub']
	search_fields = ['titulo']
	date_hierarchy = 'fecha_pub'


admin.site.register(Categoria)
admin.site.register(Post, PostAdmin)