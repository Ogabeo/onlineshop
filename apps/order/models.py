from django.db import models
from apps.base.models import BaseModel

# Create your models here.
class Sevimlilar(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name="sevimlilar")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.product}"

class Order(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    status = models.BooleanField(default = False)
    
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user} - {self.product}"

class Payment(BaseModel):
    order = models.ManyToManyField(Order, related_name='payment')
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.order}"
    
    @property
    def total(self):
        total = 0
        for order in self.order.all():
            total += order.product.get_new_price + order.quantity
        return total

class DetailReviewView(BaseModel):
    pass
 

      