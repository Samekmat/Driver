from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, generics

from .forms import RegisterForm, LoginForm
from .models import Question, Answer, Advice, Category
from .serializers import QuestionSerializer, AnswerSerializer, AdviceSerializer, CategorySerializer, UserSerializer


class QuestionListView(viewsets.ModelViewSet):
    """List of questions"""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionAPIView(APIView):
    """APIView displaying a question with given id"""

    def get(self, request, question_id):
        question = Question.objects.get(pk=question_id)

        serializer = QuestionSerializer(question)
        return Response(serializer.data)


class AnswerListView(viewsets.ModelViewSet):
    """List of answers"""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerAPIView(APIView):
    """APIView displaying an answer with given id"""

    def get(self, request, answer_id):
        answer = Answer.objects.get(pk=answer_id)

        serializer = AnswerSerializer(answer)
        return Response(serializer.data)


class CategoryListView(viewsets.ModelViewSet):
    """"List of categories"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIView(APIView):
    """APIView displaying a category with given id"""

    def get(self, request, category_id):
        category = Category.objects.get(pk=category_id)

        serializer = CategorySerializer(category)
        return Response(serializer.data)


class AdviceListView(viewsets.ModelViewSet):
    """List of advices"""

    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer


class AdviceAPIView(APIView):
    """APIView displaying an advice with given id"""

    def get(self, request, advice_id):
        advice = Advice.objects.get(pk=advice_id)

        serializer = AdviceSerializer(advice)
        return Response(serializer.data)


class UserCreate(generics.CreateAPIView):
    """CreateAPIView creates user in ApiView"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class RegisterFormView(FormView):
    """FormView for user registration by form"""

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
        return render(request, 'register.html', {'form': form})


class LoginView(View):
    """Standard view for user login by form"""
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'form': form, 'error': "User can't be found"})


class LogoutView(View):
    """LogoutView for possibility to log out user"""
    def get(self, request):
        logout(request)
        return redirect(reverse('login-form'))


class IndexView(View):
    def get(self, request):

        return render(request, 'index.html')
