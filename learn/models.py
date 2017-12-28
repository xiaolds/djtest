from datetime import datetime

from django.db import models

class File(models.Model):
    file_name = models.CharField(max_length=200)

    file_create_time = models.DateTimeField('Date file register', default=datetime.now())
    file_update_time = models.DateTimeField('Date file update', default=datetime.now())
    owner = models.ForeignKey('auth.User', related_name='files', on_delete=models.CASCADE)

    class Meta:
        ordering = ('file_create_time',)

    def __str__(self):
        return self.file_name

    def __unicode__(self):
        return '%d: %s' % (self.id, self.file_name)


