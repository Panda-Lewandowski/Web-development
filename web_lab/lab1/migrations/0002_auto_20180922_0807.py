# Generated by Django 2.0.2 on 2018-09-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]