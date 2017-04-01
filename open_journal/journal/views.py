from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView


class JournalView(TemplateView):
	template_name = "journal/journal.html"