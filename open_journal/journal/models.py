from django.db import models
from django.forms import ModelForm, SelectDateWidget
import datetime

# Create your models here.
class JournalEntry(models.Model):
	title = models.CharField(blank=False, max_length=50)
	pub_date = models.DateTimeField(blank=False)
	content = models.TextField(blank=False, max_length=3000)

class JournalForm(ModelForm):
	class Meta:
		model = JournalEntry
		fields = '__all__'
		labels = {
			'title': 'Title',
			'pub_date': 'Time',
			'content': 'Content',
		}
		help_texts = {
			'content': 'Write your journal entry here!',
		}
		widgets = {
			'pub_date': SelectDateWidget(years=range(2015, datetime.datetime.now().year))
		}