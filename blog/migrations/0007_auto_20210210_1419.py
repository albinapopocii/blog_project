# Generated by Django 3.1.3 on 2021-02-10 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210210_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='subscribe_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]