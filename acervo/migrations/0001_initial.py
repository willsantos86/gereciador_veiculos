# Generated by Django 4.1.3 on 2022-11-29 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Versao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=30, verbose_name='Cor')),
                ('motor', models.CharField(max_length=3, verbose_name='Motor')),
                ('portas', models.CharField(choices=[('2', '2 portas'), ('4', '4 portas')], max_length=2, verbose_name='Portas')),
                ('cambio', models.CharField(choices=[('manual', 'Manual'), ('auto', 'Automático')], max_length=10, verbose_name='Cambio')),
                ('combustivel', models.CharField(choices=[('gasolina', 'Gasolina'), ('alcool', 'Álcool'), ('diesel', 'diesel'), ('flex', 'Flex')], max_length=10, verbose_name='Combustivel')),
                ('ano_versao', models.IntegerField(verbose_name='Ano da Versão')),
            ],
        ),
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=10, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=10, verbose_name='Modelo')),
                ('ano_fabricacao', models.IntegerField(verbose_name='Ano de Fabricação')),
                ('chassis', models.CharField(max_length=30, unique=True, verbose_name='Chassis')),
                ('versao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acervo.versao', verbose_name='Versão')),
            ],
        ),
    ]