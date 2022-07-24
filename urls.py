from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter(trailing_slash=False)
router.register('', views.QuestionnaireViewset, basename='questionnaire')
router.register('user-answers/', views.UserResponseViewset, basename='user-answers')

urlpatterns = router.urls + [

]
