# Generated by Django 4.0.6 on 2022-08-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoHindiApp', '0002_notes_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='thumbnail',
            field=models.ImageField(upload_to='images/'),
        ),
    ]