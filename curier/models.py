from django.db import models
from django.conf import settings

class Curier(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="mycurier")
	date_of_birth=models.DateField(blank=True, null=True)
	photo =models.ImageField(upload_to='curiers/%y/%m/%d', blank=True)
	experience=models.IntegerField(blank=True, null=True)
	phone = models.IntegerField(null=False, blank=False)
	is_available=models.BooleanField(default=False)
	balance = models.DecimalField(decimal_places=0,max_digits=1000,default=0)

	def __str__(self):
		return self.user.username