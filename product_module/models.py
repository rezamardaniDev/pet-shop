from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="نام")
    descrtiption = models.TextField(verbose_name="توضیحات")
    price = models.IntegerField(verbose_name="قیمت", null=True)
    count = models.IntegerField(verbose_name="تعداد")
    description = models.TextField(verbose_name="توضیحات")
    is_active = models.BooleanField(verbose_name="موجود / ناموجود")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["price"]
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"