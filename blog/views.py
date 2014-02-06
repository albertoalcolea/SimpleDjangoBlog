# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator

from blog.models import Post


class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'latest_posts_list'
	paginate_by = 2

	def get_queryset(self):
		"""
		Return the last ten published post (not including those set to be
		published in the future).
		"""
		return Post.objects.filter(
			fecha_pub__lte=timezone.now()
		).order_by('-fecha_pub')[:5]


class DetailView(generic.DetailView):
	model = Post
	template_name = 'blog/detail.html'

	def get_queryset(self):
		"""
		Excludes any posts that aren't published yet.
		"""
		return Post.objects.filter(fecha_pub__lte=timezone.now())