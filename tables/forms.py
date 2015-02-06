from django import forms
from models import Room, User
from django.utils import timezone

class RoomForm(forms.ModelForm):
	number = forms.IntegerField()
	department = forms.CharField()
	capacity = forms.IntegerField()
	date_create = forms.DateField(initial=timezone.now(), input_formats=['%Y-%m-%d'])

	class Meta:
		model = Room
		fields = ('number','department','capacity','date_create')

class UserForm(forms.ModelForm):
	room = forms.CharField()
	name = forms.CharField()
	salary = forms.IntegerField()
	date_admit = forms.DateTimeField(initial=timezone.now(), input_formats=['%Y-%m-%d %H:%M'])

	class Meta:
		model = Room
		fields = ('room','name','salary','date_admit')