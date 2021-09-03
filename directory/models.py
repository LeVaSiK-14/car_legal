from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=127, default='')

    def __str__(self):
        return self.name

class Mark(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='marks')
    name = models.CharField(max_length=127, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'