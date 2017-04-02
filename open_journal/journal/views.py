from django.shortcuts import render, redirect, get_object_or_404
from .models import JournalForm, JournalEntry
from django.http import HttpResponse

# Create your views here.

def journal_write(request):
	complete = False
	if request.method == 'GET':
		form = JournalForm()
	else:
		form = JournalForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.writer = request.user
			model_instance.save()
			form = JournalForm()
			complete = True
	journal = JournalEntry.objects.all().order_by('-pub_date', 'title')
	return render(request, 'journal/journal.html', {'form': form, 'complete': complete, 'journal': journal})

def journal_detail(request, entry_id):
	entry = get_object_or_404(JournalEntry, pk=entry_id)
	is_writer = entry.writer == request.user
	return render(request, 'journal/detail.html', {'entry': entry, 'isWriter': is_writer})