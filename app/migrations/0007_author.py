# Generated by Django 4.2.2 on 2023-07-03 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_location_jobpost_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('mail', models.EmailField(max_length=70)),
                ('area', models.CharField(max_length=70)),
            ],
        ),
    ]
