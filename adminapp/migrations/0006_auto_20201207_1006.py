# Generated by Django 3.1.4 on 2020-12-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_auto_20201207_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]