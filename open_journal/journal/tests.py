from django.test import LiveServerTestCase
from selenium import webdriver

# Create your tests here.
class HeaderTestCase(LiveServerTestCase):
	def setUp(self):
		driver = webdriver.Chrome()
		driver.get()