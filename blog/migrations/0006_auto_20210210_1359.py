# Generated by Django 3.1.3 on 2021-02-10 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_subscribe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribe',
            old_name='email',
            new_name='subscribe_email',
        ),
    ]
