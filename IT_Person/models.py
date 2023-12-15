from django.db import models

class Pemails(models.Model):
    pemail = models.EmailField('phishing email',max_length=120,)
    apppwd = models.CharField(max_length=100)

    def __str__(self):
        return self.pemail