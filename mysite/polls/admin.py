from django.contrib import admin
from polls.models import Choice, Question

# class ChoiceInLine(admin.StackedInline): Displays in a stacked manner
class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin) :
	fieldsets = [
	    (None,               {'fields' : ['question_text']}),
	    ('Date information', {'fields' : ['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInLine]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
   

# Register your models here.
admin.site.register(Question, QuestionAdmin)


# admin.site.register(Choice)