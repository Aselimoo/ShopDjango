from django.db import models
from django.contrib.auth.models import User
from .utils import valid_price, validate_phone_number

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Категория")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    image = models.ImageField(upload_to='product/')
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.CharField(default=10.0, verbose_name="Цена", validators=[valid_price], max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.title} - {self.category} - {self.created_at}"
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    image = models.ImageField(upload_to='profile/', verbose_name="Фото профиля", help_text="Фото должно быть Х на Х", 
        blank=True, null=True)
    description = models.TextField(max_length=200, verbose_name="Информация", blank=True, null=True)
    birth_data = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", validators=[validate_phone_number], 
        blank=True, null=True)

