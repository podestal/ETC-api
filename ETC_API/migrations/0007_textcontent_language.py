# Generated by Django 5.0.6 on 2024-07-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ETC_API', '0006_textcontent_content_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='textcontent',
            name='language',
            field=models.CharField(default='javascript', max_length=255),
        ),
    ]
