from rest_framework import serializers
from . import models

class GetTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Topic
        fields = ['id', 'name', 'description']

class GetPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'topic', 'created_at']

class GetSimpleTextContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TextContent
        fields = ['id',  'content']


class GetSectionSerializer(serializers.ModelSerializer):

    content = GetSimpleTextContentSerializer(many=True)

    class Meta:
        model = models.Section
        fields = ['id', 'title', 'post', 'content']

class CreateSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Section
        fields = ['id', 'title', 'post']

class GetTextContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TextContent
        fields = '__all__'

