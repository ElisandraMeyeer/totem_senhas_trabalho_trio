# Generated by Django 4.0.5 on 2022-06-11 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totem',
            name='horario',
            field=models.DateTimeField(),
        ),
    ]
