from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('questions', views.QuestionListView)
router.register('answers', views.AnswerListView)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<int:pk>/', views.QuestionAPIView.as_view()),
    path('answers/<int:pk>/', views.AnswerAPIView.as_view()),
    ]
