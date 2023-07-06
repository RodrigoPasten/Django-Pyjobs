from django.db import models

# declaramos la constante contenedora de las opciones
NEWLETTER_OPTION = [
    ("W", "Weekly"),
    ("M", "Monthly")
]


class Subscribe(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    option = models.CharField(max_length=2, choices=NEWLETTER_OPTION, default="W")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
