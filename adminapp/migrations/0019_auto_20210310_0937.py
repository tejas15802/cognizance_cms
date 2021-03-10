# Generated by Django 3.1.4 on 2021-03-10 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0018_auto_20210302_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='organiser',
            field=models.CharField(choices=[('Sanjai Siddharthan', 'Sanjai Siddharthan'), ('Sanjay', 'Sanjay'), ('TEJENDRA SARADHI', 'TEJENDRA SARADHI'), ('Test', 'Test'), ('XAVIER EMMANUEL  E', 'XAVIER EMMANUEL  E'), ('Naresh Kumar', 'Naresh Kumar'), ('Sanjay', 'Sanjay')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='evaluator',
            field=models.CharField(choices=[('Sanjai Siddharthan', 'Sanjai Siddharthan'), ('Sanjay', 'Sanjay'), ('TEJENDRA SARADHI', 'TEJENDRA SARADHI'), ('Test', 'Test'), ('XAVIER EMMANUEL  E', 'XAVIER EMMANUEL  E'), ('Naresh Kumar', 'Naresh Kumar'), ('Sanjay', 'Sanjay')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.CharField(choices=[('Sanjai Siddharthan', 'Sanjai Siddharthan'), ('Sanjay', 'Sanjay'), ('TEJENDRA SARADHI', 'TEJENDRA SARADHI'), ('Test', 'Test'), ('XAVIER EMMANUEL  E', 'XAVIER EMMANUEL  E'), ('Naresh Kumar', 'Naresh Kumar'), ('Sanjay', 'Sanjay')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.CharField(max_length=4000, null=True)),
                ('posted_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('thumbnail', models.ImageField(upload_to='blogs/thumbnails')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='adminapp.member')),
            ],
        ),
    ]
