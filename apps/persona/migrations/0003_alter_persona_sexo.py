# Generated by Django 4.1.3 on 2022-12-02 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_alter_persona_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], default='Femenino', max_length=10),
        ),
    ]
