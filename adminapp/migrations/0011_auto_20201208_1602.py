# Generated by Django 3.1.4 on 2020-12-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_auto_20201208_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='group',
            field=models.CharField(choices=[('administrator', 'administrator'), ('member', 'member'), ('Cyber Security', 'Cyber Security')], max_length=200, null=True),
        ),
    ]