from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lng = models.DecimalField(max_digits=8, decimal_places=6)

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class User(models.Model):
    ROLES = [
        ('admin', 'Администратор'),
        ('moderator', 'Модератор'),
        ('member', 'Пользователь')
    ]

    first_name = models.CharField(max_length=100, verbose_name="Имя", null=True)
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", null=True)
    username = models.CharField(max_length=100, verbose_name="Логин", unique=True)
    password = models.CharField(max_length=100, verbose_name="Пароль")
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)
    role = models.CharField(choices=ROLES, default='member', max_length=10)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f'{self.first_name} ({self.last_name})'
