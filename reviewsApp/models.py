from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class resturants(models.Model):
    res_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.res_name


class review(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(max_length=2000, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    resturant = models.ForeignKey(resturants,
                                  on_delete=models.CASCADE,
                                  null=True)

    def __str__(self):
        return self.title
