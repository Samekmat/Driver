from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('questions', views.QuestionListView)
router.register('answers', views.AnswerListView)
router.register('categories', views.CategoryListView)
router.register('advices', views.AdviceListView)

urlpatterns = [
    path('', include(router.urls), name='main'),
    path('questions/<int:pk>/', views.QuestionAPIView.as_view()),
    path('answers/<int:pk>/', views.AnswerAPIView.as_view()),
    path('categories/<int:pk>/', views.CategoryAPIView.as_view()),
    path('advices/<int:pk>/', views.AdviceAPIView.as_view()),
    path('register/', views.UserCreate.as_view()),
    path('register/form/', views.RegisterFormView.as_view(), name='register-form'),
    path('login/form/', views.LoginView.as_view(), name='login-form'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('index/', views.IndexView.as_view(), name='index'),
    ]
