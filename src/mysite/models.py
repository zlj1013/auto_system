from django.db import models
# Create your models here.

    
class School(models.Model):
    '''
    学校表
    '''
    name=models.CharField(max_length=50,verbose_name='学校名字')
    address=models.CharField(max_length=100,verbose_name='学校地址')

    class Meta:
        verbose_name='学校'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name