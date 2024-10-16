from django.db import models
from datetime import datetime

# python manage.py makemigrations
# python manage.py migrate

class Kyrs(models.Model):
    data_vrem = models.DateTimeField('когда', null=True, default=datetime.now)
    kyrs = models.CharField('курс', max_length=100, blank=True, null=True)


    def __str__(self):
        return 'курс'

    def get_absolute_url(self):
        return f"/{self.id}"