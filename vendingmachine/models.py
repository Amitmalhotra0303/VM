from django.db import models

class vending_machine(models.Model):

    itemName = models.CharField(max_length = 100)
    itemPrice = models.IntegerField()
    itemInStock = models.IntegerField()
    image = models.URLField()

    def __str__(self):
        return self.itemName 


    
