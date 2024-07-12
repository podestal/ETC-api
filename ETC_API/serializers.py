from rest_framework import serializers
from core.serializers import GetUserSerializer
from . import models


class GetTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Topic
        fields = ['id', 'name', 'description', 'color']

class GetPostSerializer(serializers.ModelSerializer):

    created_by = GetUserSerializer()

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'topic', 'created_at', 'description', 'created_by', 'img_url']

class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'topic', 'created_at', 'description', 'img_url']

    def create(self, validated_data):
        user = self.context['user']
        return models.Post.objects.create(created_by=user, **validated_data)


class GetSimpleTextContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TextContent
        fields = ['id',  'content', 'content_type', 'language']


class GetSectionSerializer(serializers.ModelSerializer):

    content = GetSimpleTextContentSerializer(many=True)

    class Meta:
        model = models.Section
        fields = ['id', 'title', 'post', 'content', 'created_at']

class CreateSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Section
        fields = ['id', 'title', 'post', 'created_at']

class GetTextContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TextContent
        fields = '__all__'

