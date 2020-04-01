from django.contrib import admin

from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
    #This particular change above makes the “Publication date” come before the “Question” field

#to split the form up into fieldsets:
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question information',{'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date','was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)