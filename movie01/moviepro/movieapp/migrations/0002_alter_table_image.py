# Generated by Django 4.1.7 on 2023-03-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
