from django.db import models
from users.models import CustomUser
# Create your models here.
   
   
class Questionnaire(models.Model):
    name = models.CharField(max_length=200)
    for_members = models.BooleanField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
        
    def __str__(self) -> str:
        return f"{self.name}"
    
class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.question}"
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.RESTRICT)
    answer = models.BooleanField()
    full_details = models.TextField(null=True)
    
    def __str__(self) -> str:
        return f"{self.question}--{self.answer}"
    
class UserResponse(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.RESTRICT)
    response = models.ForeignKey(Answer, on_delete=models.CASCADE)
        
    def __str__(self) -> str:
        return f"{self.user}"
    
class AdditionalInformation(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    additional_information = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.answer}"
    
    
