from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import QuizCreateAPIView,QuizListView




urlpatterns = [

    path('listquiz/',QuizListView.as_view(), name='quizlist-view'),
    path('createquiz/',QuizCreateAPIView.as_view(),name='createquiz'),



]