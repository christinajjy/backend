from django.db import models

class Pemails(models.Model):
    pemail = models.EmailField('phishing email',max_length=120,)
    apppwd = models.CharField(max_length=100)

    def __str__(self):
        return self.pemail
    
class Pemails_content(models.Model):
    pemail = models.EmailField('phishing email',max_length=120)
    emp_name = models.CharField('emp_name',max_length=100,blank = True,null=True)
    emp_email = models.CharField('emp_email',max_length=250,blank = True,null=True)
    recent_project = models.CharField('recent_project',max_length=100,blank = True,null=True)
    #content = models.TextField(max_length=1000)

    def __str__(self):
        return self.pemail