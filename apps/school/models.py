from django.db import models
from apps.users.models import BaseModel
from apps.area.models import City, Province

CATEGORY_CHOICES = (
    ('ptbk', '普通本科'),
    ('dlxy', '独立学院'),
    ('zk', '专科（高职）'),
    ('qt', '其他')
)

TAG_CHOICES = (
    ('wu', ' '),
    ('gb', '公办'),
    ('211gc', '211工程'),
    ('985gc', '985工程'),
    ('yldx', '一流大学建设高校')
)


class School(BaseModel):
    name = models.CharField(verbose_name="学校名称", max_length=20)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=u"所属省份", default=1)
    category = models.CharField(verbose_name="办学类型", choices=CATEGORY_CHOICES, max_length=4, default="ptbk")
    heat_rank = models.IntegerField(verbose_name="全国热度排名", default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=u"所在地", default=1)
    tag = models.CharField(verbose_name="标签", choices=TAG_CHOICES, default="wu", max_length=5)
    tag1 = models.CharField(verbose_name="标签1", choices=TAG_CHOICES, default="wu", max_length=5)
    tag2 = models.CharField(verbose_name="标签2", choices=TAG_CHOICES, default="wu", max_length=5)
    tag3 = models.CharField(verbose_name="标签3", choices=TAG_CHOICES, default="wu", max_length=5)
    desc = models.TextField(verbose_name="学校概况", default=u"大学")

    class Meta:
        verbose_name = "学校信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class College(BaseModel):
    school = models.ForeignKey(School, verbose_name="所属学校", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="学院名称", max_length=20)
    desc = models.TextField(verbose_name="学院简介", default=u"学院")

    class Meta:
        verbose_name = "学院信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class AdmissionsCategory(BaseModel):
    school = models.ForeignKey(School, verbose_name="所属学校", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="招生名称", max_length=20)
    desc = models.TextField(verbose_name="招生名称介绍", default=u"招生名称")

    class Meta:
        verbose_name = "招生名称"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Professional(BaseModel):
    school = models.ForeignKey(School, verbose_name="所属学校", on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE, verbose_name="所属学院")
    name = models.CharField(verbose_name="专业名称", max_length=20)
    admissionscategory = models.ForeignKey(AdmissionsCategory, verbose_name="招生名称",
                                           on_delete=models.CASCADE)
    desc = models.TextField(verbose_name="专业概况", default="专业")

    class Meta:
        verbose_name = "专业信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
