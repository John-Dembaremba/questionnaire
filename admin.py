# from django.contrib import admin
# from .models import Questionnaire, Question, UserResponse, ResponseOption
# from users.models import CustomUser
# # Register your models here.  
  
# class InLineQuestion(admin.TabularInline):
#     model = Question
#     extra = 1  
    
# class QuestionnaireAdmin(admin.ModelAdmin):
#     list_display = ('name', 'for_members', 'created_date')
#     list_filter  = ('name', 'for_members', 'created_date')
#     search_fields = ("name",)
#     list_per_page = 30
#     fieldsets = (
#         (None, {'fields': ('name', 'questions')}),
#     )

# class UserResponseAdmin(admin.ModelAdmin):
#     def respondents(self, obj):
#         user = CustomUser.objects.get(username=obj.user)
#         return user.full_name
#     list_display = ('respondents', 'questionnaire',)
#     list_filter  = ('user', 'questionnaire', )
#     search_fields = ("questionnaire__name", "user__username", "user__first_name", "user__last_name")
#     list_per_page = 30
#     fieldsets = (
#         (None, {'fields': ('user', 'questionnaire', 'response')}),
#     )


# admin.site.register(Questionnaire, QuestionnaireAdmin)
# admin.site.register(UserResponse, UserResponseAdmin)












