from django.shortcuts import render, redirect
from .models import JournalForm
from django.http import HttpResponse

# Create your views here.


def journal_write(request):
	if request.method == 'GET':
		form = JournalForm()
	else:
		form = JournalForm(request.POST)
		if form.is_valid():
			model_instance = form.save()
			return redirect(journal_overview)
	return render(request, 'journal/journal.html', {'form': form})

def journal_overview(request):
	return HttpResponse('Journal Entry overview')