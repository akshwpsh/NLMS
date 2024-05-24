from django.db import models
from django.contrib.auth.models import User

# 그룹 : 교수, 학생, (관리자)
class Group(models.Model): # 그룹
    name = models.CharField(max_length=100)

class Profile(models.Model): # 프로필
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    userID = models.IntegerField(null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)