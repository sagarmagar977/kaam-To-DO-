from django.db import models

# Create your models here.
def tets():
    pass
status_list=[('गरियो', 'गरियो'),('गर्दै','गर्दै'),('गरेको छैन','गरेको छैन')]
#two tuples of same data are made for read and write of the same data !
class ToDo(models.Model):
    name = models.CharField(max_length=300,blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    status = models.CharField(max_length=50,choices=status_list,blank=False, null=False)

    def __str__(self):
        return self.name