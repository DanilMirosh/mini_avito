from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=150)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=1000)
    is_published = models.BooleanField(default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name
