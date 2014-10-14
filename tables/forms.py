from django import forms
from models import Room, User
from django.utils import timezone

class RoomForm(forms.ModelForm):
	number = forms.IntegerField()
	department = forms.CharField()
	capacity = forms.IntegerField()
	date_create = forms.DateField(initial=timezone.now())

	class Meta:
		model = Room
		fields = ('number','department','capacity','date_create')