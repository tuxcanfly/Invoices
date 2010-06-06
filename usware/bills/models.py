from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here

class Invoice(models.Model):
	date = models.DateTimeField('date_purchased')
	description = models.TextField()
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return str(self.id)

class InvoiceForm(ModelForm):
	class Meta:
		model = Invoice

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name')
