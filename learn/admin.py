from django.contrib import admin

from learn.models import Question, User, Choice

admin.site.register(Question)
admin.site.register(User)
admin.site.register(Choice)
