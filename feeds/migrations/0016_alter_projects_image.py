# Generated by Django 3.2.16 on 2023-08-18 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0015_alter_about_about_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
