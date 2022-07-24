# from  .serializers import QuestionnaireSerializer, UserResponseSerializer
# from .models import Questionnaire, Question, UserResponse
# from users.models.users import CustomUser
# from rest_framework import permissions
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import viewsets
# from rest_framework.response import Response


# class QuestionnaireViewset(viewsets.ModelViewSet):
#     queryset = Questionnaire.objects.all()
#     serializer_class = QuestionnaireSerializer
#     permission_classe = [permissions.IsAuthenticated]
#     filter_backends = [DjangoFilterBackend]


# class UserResponseViewset(viewsets.ModelViewSet):
#     queryset = UserResponse.objects.all()
#     serializer_class = UserResponseSerializer
#     permission_classe = [permissions.IsAuthenticated]
#     filter_backends = [DjangoFilterBackend]

#     def create(self, request, *args, **kwargs):
#         """
#         Listening to post request:
#         --> check if user is a member if questionnaire is for members
#         --> check if full details are provided if member's answere is true
#         """
#         data = request.data
#         response_details = data['response']
#         questionnaire_obj = Questionnaire.objects.get(pk=data["questionnaire"])
#         questionnaire_members = questionnaire_obj.for_members
        
#         if questionnaire_members:
#             user = data['user']
#             user_obj = CustomUser.objects.get(pk=user)
#             member = user_obj.is_member
            
#             if member:
#                 for response in response_details:
#                     # Check if each answer(True) has full details
#                     answer = response["answer"]
                    
#                     if answer:
#                         details = response['full_details']
#                         if details == None:
#                             question_obj = Question.objects.get(pk=response["question"])
#                             question = question_obj.question
#                             data = {
#                                 "question": question,
#                                 "answer": answer,
#                                 "message": "Please provide full details for your answer."
#                                 }
#                             return Response(data=data, status=400)                       
#                 return super().create(request, *args, **kwargs)
#             else:
#                 return Response(data={"message": "Sorry, the questionnaire is for members only"}, status=400)
#         else:
#             return super().create(request, *args, **kwargs)

        
        
    
        
        
    


