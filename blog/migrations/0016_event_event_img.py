# Generated by Django 3.1.3 on 2021-02-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210212_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
