from django.db import models


class DataTruck(models.Model): 
    temperature = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True  
    )
    gas = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True  
    )
    magnetic = models.DecimalField(
        max_digits=5, decimal_places=0, null=True, blank=True  
    )
    pressure = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True  
    )
    humidity = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True  
    )
    created_at = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return f'{self.name}-{self.branch.name}'  

    class Meta:
        verbose_name = 'Данные' 
        verbose_name_plural = 'Данные' 
