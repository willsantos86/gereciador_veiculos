# Generated by Django 4.1.3 on 2022-11-29 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acervo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carros',
            new_name='Carro',
        ),
        migrations.AlterModelOptions(
            name='carro',
            options={'verbose_name_plural': 'Carros'},
        ),
        migrations.AlterModelOptions(
            name='versao',
            options={'verbose_name_plural': 'Versões'},
        ),
    ]
