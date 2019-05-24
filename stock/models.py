from django.db import models

# Create your models here.


class Product(models.Model):

    name = models.CharField('Nome do produto', max_length=50)
    quantity = models.IntegerField('Quantidade')
    price = models.DecimalField('Preço', max_digits=7, decimal_places=2)

    def __str__(self):
        return self.quantity

    class Meta:
        verbose_name = 'Produto'
