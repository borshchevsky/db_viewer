from django.db import models


class DB(models.Model):
    host = models.CharField(max_length=255)
    port = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    schema = models.JSONField()
    type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.type.capitalize} DB'
