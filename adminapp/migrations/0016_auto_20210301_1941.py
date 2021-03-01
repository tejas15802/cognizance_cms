# Generated by Django 3.1.4 on 2021-03-01 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0015_auto_20210201_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='organiser',
            field=models.CharField(choices=[('Naresh Kumar', 'Naresh Kumar'), ('Sanjay', 'Sanjay'), ('Tejendra Saradhi', 'Tejendra Saradhi')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='evaluator',
            field=models.CharField(choices=[('Naresh Kumar', 'Naresh Kumar'), ('Sanjay', 'Sanjay'), ('Tejendra Saradhi', 'Tejendra Saradhi')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.CharField(choices=[('Naresh Kumar', 'Naresh Kumar'), ('Sanjay', 'Sanjay'), ('Tejendra Saradhi', 'Tejendra Saradhi')], max_length=200, null=True),
        ),
    ]
