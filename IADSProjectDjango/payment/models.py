from django.db import models


class Order(models.Model):
    CURR_CHOICES = [
        ('CAD', 'Canadian Dollar'),
        ('USD', 'US Dollar'),
        ('CNY', 'China Yuan'), ]
    order_id = models.CharField(max_length=50)
    amount = models.IntegerField()
    currency = models.CharField(max_length=3, choices=CURR_CHOICES)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=50)
    order_user = models.CharField(max_length=50)

    def __str__(self):
        return self.order_id
