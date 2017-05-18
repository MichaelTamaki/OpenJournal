from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
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
	if not request.user.is_authenticated:
		journal = None
	else:
		journal = JournalEntry.objects \
			.filter(Q(writer__exact=request.user) | Q(public__exact=True)) \
			.order_by('-pub_date', 'title')
	return render(request, 'journal/journal.html', {'form': form, 'complete': complete, 'journal': journal})

def journal_detail(request, entry_id):
	entry = get_object_or_404(JournalEntry, pk=entry_id)
	canView = entry.writer == request.user or entry.public
	return render(request, 'journal/detail.html', {'entry': entry, 'canView': canView})