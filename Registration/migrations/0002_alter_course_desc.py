# Generated by Django 4.0.5 on 2022-12-21 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='desc',
            field=models.CharField(max_length=10),
        ),
    ]
