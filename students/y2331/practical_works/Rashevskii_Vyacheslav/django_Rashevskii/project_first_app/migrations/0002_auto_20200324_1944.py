# Generated by Django 3.0.4 on 2020-03-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
