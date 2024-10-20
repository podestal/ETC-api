from django.db import models
from django.conf import settings


class Topic(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    color = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    img_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Section(models.Model):

    title = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TextContent(models.Model):

    TYPE_TEXT = "T"
    TYPE_CODE = "C"
    TYPE_IMG = "I"

    TYPE_CHOICES = [
        (TYPE_TEXT, "Text"),
        (TYPE_CODE, "Code"),
        (TYPE_IMG, "Img"),
    ]

    TYPE_JAVASCRIPT = "javascript"
    TYPE_PYTHON = "python"

    LANGUAGE_CHOICES = [(TYPE_JAVASCRIPT, "JavaScript"), (TYPE_PYTHON, "Python")]

    content = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="content")
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.CharField(max_length=1, default="T", choices=TYPE_CHOICES)
    language = models.CharField(max_length=255, null=True, blank=True, choices=LANGUAGE_CHOICES)
