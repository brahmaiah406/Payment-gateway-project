from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class GenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
	serializer_class = ArticleSerializer
	queryset = Article.objects.all()
	lookup_field = 'id'

	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, id = None):

		if id:
			return self.retrieve(request)
		else:
			return self.list(request)

	def post(self, request):
		return self.create(request)

	def put(self, request, id=None):
		return self.update(request, id)

	def delete(self, request, id):
		return self.destroy(request, id)

		

