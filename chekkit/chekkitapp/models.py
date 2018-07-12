from django.db import models

# Create your models here.
class Manufacturer(models.Model):
	name = models.CharField(max_length=100)
	code = models.IntegerField(default=0, blank=True, null=True, unique=True)
	email = models.EmailField()
	phonenumber = models.CharField(max_length=20)
	industry = models.CharField(max_length=100)
	address = models.CharField(max_length=255)
	created_on = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=False)

	class Meta:
		ordering =['-created_on']

	def __unicode__(self):
		return u'{} Code:{} Phone:{} Email:{} industry:{} address:{}'.format(self.name, str(self.code),self.phonenumber, self.email, self.industry, self.address)


class Product(models.Model):
	name = models.CharField(max_length=100)
	photo = models.ImageField(upload_to = 'images', blank=True)
	description = models.TextField(blank=True, null=True)
	production_date = models.DateTimeField(auto_now_add=True)
	quantity = models.IntegerField(default=0, blank=True, null=True)
	manufacturer_id =models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=False)


	class Meta:
		ordering =['-created_on']

	def __unicode__(self):
		return u'{} Photo:{} Description:{}'.format(self.name, self.photo,self.description)


class Batches(models.Model):
	batch_number = models.CharField(max_length=100, blank=True, null=True)
	product_id =models.ForeignKey('Product', on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=False)


	class Meta:
		ordering =['-created_on']

	def __unicode__(self):
		return self.batch_number


class Items(models.Model):
	item_code = models.CharField(max_length=100, unique=True)
	batch_id= models.ForeignKey('Batches', on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=False)

	class Meta:
		ordering =['-created_on']

	def __unicode__(self):
		return self.item_code
