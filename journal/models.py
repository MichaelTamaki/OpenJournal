from django.db import models
from django.forms import ModelForm, SelectDateWidget, Textarea
from django.conf import settings
from django.utils import timezone
import datetime

# Create your models here.


class JournalEntry(models.Model):
	title = models.CharField(blank=False, max_length=50)
	pub_date = models.DateTimeField(default=timezone.now)
	content = models.TextField(blank=False, max_length=3000)
	writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	public = models.BooleanField(default=False)

class JournalForm(ModelForm):

	class Meta:
		model = JournalEntry
		fields = ['title', 'content', 'public']
		labels = {
			'title': 'Title',
			'content': '',
			'public': 'Make public'
		}
		widgets = {
			'content': Textarea(attrs={'placeholder': 'Type your journal entry here!'})
		}