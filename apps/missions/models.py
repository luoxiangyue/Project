# Create your models here.

from datetime import datetime

from django.db import models

from users.models import UserProfile


class Missions(models.Model):
    """
    任务
    """
    missionId = models.IntegerField(primary_key=True, default=1, verbose_name="项目编号")
    missionName = models.CharField(max_length=50, null=True, blank=True, verbose_name="任务名称")
    missionLeader = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name="任务负责人", related_name="leaderMission")
    missionMember = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name="任务成员")
    missionEndTime = models.DateTimeField(default=datetime.now, verbose_name="截止时间")
    missionDesc = models.TextField(max_length=200, null=True, blank=True, verbose_name="任务详细要求")
    missionStatus = models.BooleanField(default=0, verbose_name="任务完成状态")

    class Meta:
        verbose_name = "任务"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.missionName
