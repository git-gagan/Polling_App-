from django.db import models
from django.db.models.base import Model

# A model is a single source of truth about your data
# We will create 2 models:- One for question and one for choice
# Each choice is associated with a question

# Each model is represented by a class 
# Each class variable represents a DB field

class Question(models.Model):
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published: ")
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
