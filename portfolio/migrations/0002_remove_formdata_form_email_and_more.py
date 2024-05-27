# Generated by Django 5.0.6 on 2024-05-27 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formdata',
            name='form_email',
        ),
        migrations.RemoveField(
            model_name='formdata',
            name='form_message',
        ),
        migrations.RemoveField(
            model_name='formdata',
            name='form_name',
        ),
        migrations.AddField(
            model_name='formdata',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=32),
        ),
        migrations.AddField(
            model_name='formdata',
            name='message',
            field=models.TextField(default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formdata',
            name='name',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]