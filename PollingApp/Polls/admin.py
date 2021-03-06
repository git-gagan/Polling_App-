from django.contrib import admin

# Register your models here.
from .models import Question, Choice

#admin.site.register(Question)
admin.site.register(Choice)

#Change Admin site
class QuesAdmin(admin.ModelAdmin):
    """fields = [
        'pub_date',
        "question_text"
    ]"""
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    

admin.site.register(Question, QuesAdmin)
