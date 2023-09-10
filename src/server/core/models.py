from django.db import models


class TelegramUser(models.Model):
    first_name = models.CharField(
        max_length=80,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=80,
        verbose_name="Фамилия"
    )
    account_id = models.PositiveIntegerField(verbose_name="ID в телеграмме")
    phone_number = models.CharField(
        max_length=12,
        verbose_name="Номер телефона"
    )
