from django.db import models
from django.conf import settings
from antros.models import Antro, MenuItem

class Reservation(models.Model):
    antro = models.ForeignKey(Antro, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    #qr_code = models.CharField(max_length=250)
    #url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reservation {self.id} by {self.user}'

class ReservationItem(models.Model):
    reservation = models.ForeignKey(Reservation, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.menu_item.name} in Reservation {self.reservation.id}'

