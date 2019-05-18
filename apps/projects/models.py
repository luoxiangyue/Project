from django.db import models
from users.models import UserProfile

# Create your models here.


class Projects(models.Model):

    projectName = models.CharField(max_length=50, verbose_name="项目名称", help_text="项目名称")
    projectDesc = models.TextField(max_length=200, verbose_name="项目简介", default="")
    projectUnit = models.CharField(max_length=50, verbose_name="项目单位", null=True, blank=True)
    projectComment = models.TextField(max_length=200, verbose_name="专家项目评语", default="")
    projectLeader = models.ForeignKey(UserProfile, verbose_name="项目负责人", null=True, blank=True)

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.projectName
