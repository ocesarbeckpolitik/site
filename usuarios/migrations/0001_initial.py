# Generated by Django 4.2.1 on 2023-06-04 03:19

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigoAcademiaco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', ckeditor.fields.RichTextField()),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField(blank=True, null=True)),
                ('tiktok', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('medium', models.URLField(blank=True, null=True)),
                ('Linkedin', models.URLField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('gmail', models.URLField(blank=True, null=True)),
                ('discord', models.URLField(blank=True, null=True)),
                ('playstation', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', ckeditor.fields.RichTextField()),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SobreMim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('sobre_mim', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('cpf', models.CharField(blank=True, max_length=12, null=True)),
                ('nomeUsuario', models.CharField(blank=True, max_length=100, null=True)),
                ('usuarioEmail', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
    ]
