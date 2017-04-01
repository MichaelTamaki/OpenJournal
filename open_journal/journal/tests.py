from django.test import LiveServerTestCase, TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from .models import JournalEntry, JournalForm
from .views import journal_write
import datetime
import time

# Create your tests here.
class SeleniumTestCase(LiveServerTestCase):
	# Selenium does not use its own database, must clear what is made

	def setUp(self):
		self.driver = webdriver.Chrome()
		super(SeleniumTestCase, self).setUp()
		self.driver.implicitly_wait(10)

	def tearDown(self):
		self.driver.quit()
		for entry in JournalEntry.objects.filter(title__exact='[Test Title]'):
			entry.delete()
		super(SeleniumTestCase, self).tearDown()

	def test_initial_load(self):
		self.driver.get('http://127.0.0.1:8000/')
		header = self.driver.find_element_by_class_name('header-text').text
		title = self.driver.find_element_by_id('id_title')
		date_month = self.driver.find_element_by_id('id_pub_date_month')
		date_day = self.driver.find_element_by_id('id_pub_date_day')
		date_year = self.driver.find_element_by_id('id_pub_date_year')
		content = self.driver.find_element_by_id('id_content')
		with self.assertRaises(NoSuchElementException):
			self.driver.find_element_by_class_name('header-tex')
		self.assertEqual(header, 'Open Journal', 'header = %s' % header)

	def test_form_entry(self):
		self.driver.get('http://127.0.0.1:8000/')
		title = self.driver.find_element_by_id('id_title')
		date_month = Select(self.driver.find_element_by_id('id_pub_date_month'))
		date_day = Select(self.driver.find_element_by_id('id_pub_date_day'))
		date_year = Select(self.driver.find_element_by_id('id_pub_date_year'))
		content = self.driver.find_element_by_id('id_content')
		submit = self.driver.find_element_by_id('submit')

		title.send_keys('[Test Title]')
		date_month.select_by_index(0)
		date_day.select_by_index(0)
		date_year.select_by_index(0)
		content.send_keys('[Test Content]')
		submit.click()

		time.sleep(1)
		success = self.driver.find_element_by_class_name('success')
		self.assertEqual(success.text, 'Journal Entry Successfully submitted!')
		# journalEntry = self.driver.find_element_by_id()


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

# class HttpRequestTestCase(TestCase):
# 	def test_url_resolve(self):
# 		found = resolve('/')
# 		self.assertEqual(found, journal_write)

	# def test_initial_html(self):
	# 	request = HttpRequest()
	# 	response = journal_write(request)
	# 	html = response.content.decode('utf8')
	# 	self.assertIn( )
