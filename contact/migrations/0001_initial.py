# Generated by Django 3.1.1 on 2020-11-19 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('relationship', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=25)),
                ('address', models.TextField(max_length=80)),
                ('email', models.EmailField(max_length=60)),
            ],
        ),
    ]
