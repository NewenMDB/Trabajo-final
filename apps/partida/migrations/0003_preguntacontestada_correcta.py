# Generated by Django 3.0 on 2021-08-30 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partida', '0002_auto_20210823_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntacontestada',
            name='correcta',
            field=models.BooleanField(default=False),
        ),
    ]
