from django.db import models

PREFIX_CHOICES = (
    ('Mr.', 'Mr.'),
    ('Miss', 'Miss'),
    ('Mrs.', 'Mrs'),
    ('Ms', 'Ms')
)

#classes are usually singular with a title caps
class  profiles(models.Model):
    type = models.CharField(max_length=60, choices=PREFIX_CHOICES, default='')
    fName = models.CharField(max_length=30, default="", blank=True, null=False)
    lName = models.CharField(max_length=30, default="", blank=True, null=False)
    Email = models.CharField(max_length=60, default="")
    Username = models.CharField(max_length=30, default='', blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.fName
