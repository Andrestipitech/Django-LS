# Generated by Django 4.1.3 on 2022-12-29 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pbv',
            fields=[
                ('idpbv', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=15)),
                ('modelo', models.CharField(max_length=15)),
                ('cc', models.IntegerField()),
                ('especificaciones', models.CharField(max_length=15)),
            ],
        ),
    ]
