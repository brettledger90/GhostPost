from django.db import models
import string
import random

def deleteId():
        constant = string.ascii_lowercase
        result = ''
        for i in range(6):
            result += random.choice(constant)

        return result

class Post(models.Model):
    Boast = 'Boast'
    Roast = 'Roast'

    POST_CHOICES = [
        (Boast, 'Boast'),
        (Roast, 'Roast')
    ]


    body = models.CharField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)
    dislike = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    typeOfPost = models.CharField(choices=POST_CHOICES, default=Boast, max_length=5)
    delete = models.CharField(default=deleteId, max_length=6, editable=False)

    def __str__(self):
        return self.body