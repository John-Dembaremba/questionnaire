# from .models import *
# from rest_framework import serializers
# from drf_writable_nested import WritableNestedModelSerializer

# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = "__all__"


# class QuestionnaireSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
#     questions = QuestionSerializer(many=True, )
#     class Meta:
#         model = Questionnaire
#         fields = ["id", "name", "for_members", "questions"]

        
# class ResponseOptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ResponseOption
#         fields = ["id", "question", "answer", "full_details"]
    
        
# class UserResponseSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
#     response = ResponseOptionSerializer(many=True, )
    
#     class Meta:
#         model = UserResponse
#         fields = ["id", "user", "questionnaire", "response", "other_conditions"]
            
    
    
        
    
        