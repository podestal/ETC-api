from rest_framework import serializers
from . import models

class GetTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Topic
        fields = '__all__'

class GetPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = '__all__'

class GetSimpleTextContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TextContent
        fields = ['id',  'content']


class GetSectionSerializer(serializers.ModelSerializer):

    content = GetSimpleTextContentSerializer(many=True)

    class Meta:
        model = models.Section
        fields = ['id', 'title', 'post', 'content']

class GetTextContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TextContent
        fields = '__all__'

