from django.test import LiveServerTestCase, TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from .models import JournalEntry, JournalForm
from .views import journal_write
import datetime
import time

# Create your tests here.

class JournalEntryModelTestCase(TestCase):
	def test_create_delete(self):
		title = 'Raindrop'
		pub_date = datetime.datetime(2017, 4, 1, 10, 41)
		content = 'Droptop'
		entry = JournalEntry(title=title, pub_date=pub_date, content=content)
		self.assertEqual(entry.title, title)
		self.assertEqual(entry.pub_date, pub_date)
		self.assertEqual(entry.content, content)

	def test_journal_valid_form_entry(self):
		form = JournalForm({
			'title': 'Title!',
			'pub_date': datetime.datetime(2017, 4, 1),
			'content': 'Happy April Fools Day!',
		})
		self.assertTrue(form.is_valid())
		entry = form.save()
		self.assertEqual(entry.title, 'Title!')
		date = datetime.datetime(2017, 4, 1)
		self.assertEqual(entry.pub_date.year, date.year)
		self.assertEqual(entry.content, 'Happy April Fools Day!')

	def test_journal_invalid_form_entry(self):
		form = JournalForm({
			'title': 'Invalid!',
			'pub_date': datetime.datetime(2017, 4, 1),
			'content': '',
		})
		self.assertFalse(form.is_valid())
		self.assertEqual(len(form.errors), 1)