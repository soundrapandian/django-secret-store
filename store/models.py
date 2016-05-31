from django.db import models

class SecretType(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return u'%s'%self.name

class SecretStore(models.Model):
    key = models.CharField(max_length=50)
    type = models.ForeignKey(SecretType, null=True, blank=True, on_delete=models.SET_NULL)
    value = models.CharField(max_length=100)
	
    def __unicode__(self):
        return u'%s[%s] = ****'%(self.key, self.type.name)
    
    class Meta:
        unique_together = ("key", "type")
