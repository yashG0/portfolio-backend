# Generated by Django 5.0.6 on 2024-05-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=24)),
                ('form_email', models.EmailField(max_length=255)),
                ('form_message', models.TextField(max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('project_description', models.TextField()),
                ('project_img', models.ImageField(upload_to='project_images/')),
                ('project_source_code', models.URLField()),
            ],
        ),
    ]
