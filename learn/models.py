
from django.db import models

"""
class User(models.Model):
    # user_id = models.IntegerField(primary_key=True,auto_created=True)
    user_name = models.CharField(max_length=200)
    # 1: male 2:female
    user_sex = models.IntegerField(default=1)
    user_password = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_phone = models.CharField(max_length=50)
    user_register_time = models.DateTimeField('Date user register')
    user_login_time = models.DateTimeField('Date user login')

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ('user_register_time',)
"""


class File(models.Model):
    file_name = models.CharField(max_length=200)

    file_create_time = models.DateTimeField('Date file register')
    file_update_time = models.DateTimeField('Date file update')
    owner = models.ForeignKey('auth.User', related_name='files', on_delete=models.CASCADE)



