from django.db import models

#Create your models here.

class User(models.Model):
    STATUS = [
		('Waiting', 'Waiting'),
		('TwoVar', 'TwoVar'),
		('InverseMatrix', 'InverseMatrix'),
		('HorizontalThrow', 'HorizontalThrow'),
	]
    user = models.CharField(max_length=99)
    status = models.TextField(choices=STATUS, default='Waiting')

    def __str__(self):
        return self.user