# Generated by Django 3.0.2 on 2021-01-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(max_length=20)),
                ('air', models.CharField(max_length=20)),
                ('co', models.CharField(max_length=20)),
                ('lpg', models.CharField(max_length=20)),
                ('smoke', models.CharField(max_length=20)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
