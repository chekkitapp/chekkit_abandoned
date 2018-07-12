from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class UssdRecord(models.Model):
	session_id = models.CharField(max_length=50)
	phone_no = models.CharField(max_length=15)
	gateway = models.CharField(max_length=10)
	data = JSONField(default=dict())
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
class Meta:
	unique_together = ('session_id', 'gateway')
	ordering = ['-created']
def __unicode__(self):
	return u'{}-{}'.format(self.session_id,self.phone_no)

