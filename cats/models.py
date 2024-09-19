from django.conf import settings
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Cat(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    age = models.PositiveIntegerField(verbose_name="Age")
    color = models.CharField(max_length=100, verbose_name="Color")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Владелец",
        help_text="Укажите владельца"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cat"
        verbose_name_plural = "Cats"
