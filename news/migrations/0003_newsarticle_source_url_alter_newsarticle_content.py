# Generated by Django 4.2 on 2024-01-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_newsarticle_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='source_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='content',
            field=models.TextField(),
        ),
    ]
