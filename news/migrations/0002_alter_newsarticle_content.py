# Generated by Django 4.2 on 2024-01-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='content',
            field=models.TextField(null=True),
        ),
    ]