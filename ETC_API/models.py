from django.db import models

class Topic(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()

class Post(models.Model):

    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

class Section(models.Model):

    title = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class TextContent(models.Model):

    content = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

