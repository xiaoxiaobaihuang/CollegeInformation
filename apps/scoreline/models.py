from django.db import models

from apps.area.models import Province

from apps.users.models import BaseModel

from apps.school.models import School, Professional


LEVEL_CHOICES = (
    ('bk', '本科'),
    ('zk', '专科'),
)


class Year(BaseModel):
    name = models.IntegerField(verbose_name="年份", default=2015)

    class Meta:
        verbose_name = "年份"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Batch(BaseModel):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name="所在省份")
    name = models.CharField(verbose_name="批次名", max_length=10)

    class Meta:
        verbose_name = "批次"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ProvinceScore(BaseModel):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name="所在省份")
    name = models.CharField(verbose_name="类别", max_length=10)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, verbose_name="批次")
    score = models.IntegerField(verbose_name="分数线", default=0)

    class Meta:
        verbose_name = "省控线"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ProfessionalScore(BaseModel):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, verbose_name="年份", default=1)
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="学校")
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, verbose_name="专业")
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name="省份")
    level = models.CharField(verbose_name="层次", choices=LEVEL_CHOICES, default="bk", max_length=5)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, verbose_name="批次")
    highest = models.IntegerField(verbose_name="最高分", default=0)
    lowest = models.IntegerField(verbose_name="最低分", default=0)
    average = models.FloatField(verbose_name="平均分", default=0)
    place = models.IntegerField(verbose_name="位次", default=0, null=True)
    note = models.CharField(verbose_name="备注", max_length=100, null=True)

    class Meta:
        verbose_name = "专业分数线"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{school}的{professional}专业在{province}的最低分是{lowest}".format(
            school=self.school.name, professional=self.professional.name, province=self.province.name,
            lowest=self.lowest)
