# Generated by Django 4.2.7 on 2023-12-24 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_musicmodel_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicmodel',
            name='publication_date',
            field=models.DateField(null=True),
        ),
    ]
