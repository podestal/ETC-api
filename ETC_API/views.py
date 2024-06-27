from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from . import serializers

class TopicViewSet(ModelViewSet):

    queryset = models.Topic.objects.all()
    serializer_class = serializers.GetTopicSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

class PostViewSet(ModelViewSet):

    queryset = models.Post.objects.select_related('topic', 'created_by')
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [OrderingFilter]
    ordering_fields = ['created_at']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreatePostSerializer
        return serializers.GetPostSerializer
    
    def get_serializer_context(self):
        return {'user': self.request.user}

class SectionViewSet(ModelViewSet):

    queryset = models.Section.objects.select_related('post').prefetch_related('content')
    serializer_class = serializers.GetSectionSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['post']

    def get_serializer_class(self):

        if self.request.method == 'POST':
            return serializers.CreateSectionSerializer
        return serializers.GetSectionSerializer

class TextContentViewSet(ModelViewSet):

    queryset = models.TextContent.objects.select_related('section')
    serializer_class = serializers.GetTextContentSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['section']
