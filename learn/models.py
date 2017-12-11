from datetime import datetime, timezone

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# class User(models.Model):
#     user_name = models.CharField(max_length=200)
#     # 1: male 2:female
#     user_sex = models.IntegerField(default=1)
#     user_password = models.CharField(max_length=200)
#     user_email = models.CharField(max_length=200)
#     user_phone = models.CharField(max_length=50)
#     user_register_time = models.DateTimeField('Date user register')
#     user_login_time = models.DateTimeField('Date user login')
#
#     def __str__(self):
#         return self.user_name
