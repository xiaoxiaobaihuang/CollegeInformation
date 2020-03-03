from django.db import models

from apps.users.models import BaseModel


class Province(BaseModel):
    name = models.CharField(max_length=20, verbose_name=u"省份")

    class Meta:
        verbose_name = "省份"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class City(BaseModel):
    province = models.ForeignKey(Province, verbose_name="所在省份", on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name=u"城市")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
