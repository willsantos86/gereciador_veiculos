from django.db import models

# Create your models here.
class Versao(models.Model):
    portas_list = (
        ("2", "2 portas"),
        ("4", "4 portas"),
    )
    cambio_list = (
        ("manual", "Manual"),
        ("auto", "Automático"),
    )
    combustivel_list = (
        ("gasolina", "Gasolina"),
        ("alcool", "Álcool"),
        ("diesel", "Diesel"),
        ("flex", "Flex"),
    )

    cor = models.CharField(max_length=30, verbose_name="Cor")
    motor = models.CharField(max_length=3, verbose_name="Motor")
    portas = models.CharField(max_length=2, verbose_name="Portas", choices=portas_list)
    cambio = models.CharField(max_length=10, verbose_name="Cambio", choices=cambio_list)
    combustivel = models.CharField(max_length=10, verbose_name="Combustivel", choices=combustivel_list)
    ano_versao = models.IntegerField(verbose_name="Ano da Versão")
    
    #Renomear classe
    class Meta:
        verbose_name_plural = "Versões"

    #Formato de saída.
    def __str__(self):
        return f'Versão {self.id}'

class Carro(models.Model):
    marca = models.CharField(max_length=10, verbose_name="Marca")
    modelo = models.CharField(max_length=10, verbose_name="Modelo")
    versao = models.ForeignKey(Versao, on_delete=models.CASCADE, verbose_name="Versão")
    ano_fabricacao = models.IntegerField(verbose_name="Ano de Fabricação")
    chassis = models.CharField(max_length=30, verbose_name="Chassi", unique=True)

    #Renomear classe
    class Meta: 
        verbose_name_plural = "Carros"

    #Formato de saída.
    def __str__(self):
        return f'{self.modelo} - {self.marca} - {self.chassis}'