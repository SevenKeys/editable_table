from django.db import models

class Room(models.Model):
	number = models.IntegerField()
	department = models.CharField(max_length=25)
	capacity = models.IntegerField(default=0)
	date_create = models.DateField('date_created',blank=True)

	def __unicode__(self):
		return str(self.number)

class User(models.Model):
	room = models.ForeignKey(Room)
	name = models.CharField(max_length=25)
	salary = models.IntegerField(default=0)
	date_admit = models.DateTimeField('date_admittance')

	def __unicode__(self):
		return self.name


