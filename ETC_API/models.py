from django.db import models

class Topic(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Section(models.Model):

    title = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TextContent(models.Model):

    content = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='content')

