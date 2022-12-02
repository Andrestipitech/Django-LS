# Generated by Django 4.1.3 on 2022-11-25 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0004_alter_vehiculo_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id_mate', models.AutoField(primary_key=True, serialize=False)),
                ('descipcion', models.CharField(max_length=85)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='mantenimiento',
            field=models.ManyToManyField(blank=True, to='vehiculo.mantenimiento'),
        ),
    ]