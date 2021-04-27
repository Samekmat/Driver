from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('questions', views.QuestionListView)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<int:pk>/', views.QuestionView.as_view()),
    ]
