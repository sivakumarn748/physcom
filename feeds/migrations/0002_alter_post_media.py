# Generated by Django 4.2.10 on 2024-03-31 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='media',
            field=models.FileField(blank=True, default=None, null=True, upload_to='feeds/media/'),
        ),
    ]
