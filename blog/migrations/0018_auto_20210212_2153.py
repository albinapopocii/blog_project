# Generated by Django 3.1.3 on 2021-02-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_event_first_image_keywords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employmentopportunity',
            name='employment_company',
        ),
        migrations.AddField(
            model_name='employmentopportunity',
            name='company_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='employmentopportunity',
            name='job_link',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='employmentopportunity',
            name='job_position',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.DeleteModel(
            name='EmploymentCompany',
        ),
        migrations.DeleteModel(
            name='JobOpportunity',
        ),
    ]