from django.contrib import admin

# Register your models here.
from .models import JournalEntry

class JournalAdmin(admin.ModelAdmin):
	model = JournalEntry
	list_display = ('title', 'writer')

admin.site.register(JournalEntry, JournalAdmin)
