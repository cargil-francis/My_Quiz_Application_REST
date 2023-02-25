from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import QuizCreateAPIView,QuizListAPIView, UserProfileAPIView, RegisterAPIView,QuizTakingAPIView



urlpatterns = [
    path('quiztaking/<int:quiz_id>',QuizTakingAPIView.as_view(), name='quiztaking'),
    path('listquiz/',QuizListAPIView.as_view(), name='quizlist-view'),
    path('createquiz/',QuizCreateAPIView.as_view(),name='createquiz'),
    path('userprofile/',UserProfileAPIView.as_view(),name='user-profile'),
    path('register/', RegisterAPIView.as_view(), name='register'),




]