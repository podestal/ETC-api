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


class GetSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Section
        fields = '__all__'

class GetTextContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TextContent
        fields = '__all__'

