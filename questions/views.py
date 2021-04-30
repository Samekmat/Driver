from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from .models import Question, Answer, Advice, Category
from .serializers import QuestionSerializer, AnswerSerializer, AdviceSerializer, CategorySerializer, UserSerializer


class QuestionListView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionAPIView(APIView):
    def get(self, request, question_id):
        question = Question.objects.get(pk=question_id)

        serializer = QuestionSerializer(question)
        return Response(serializer.data)


class AnswerListView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerAPIView(APIView):
    def get(self, request, answer_id):
        answer = Answer.objects.get(pk=answer_id)

        serializer = AnswerSerializer(answer)
        return Response(serializer.data)


class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIView(APIView):
    def get(self, request, category_id):
        category = Category.objects.get(pk=category_id)

        serializer = CategorySerializer(category)
        return Response(serializer.data)


class AdviceListView(viewsets.ModelViewSet):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer


class AdviceAPIView(APIView):
    def get(self, request, advice_id):
        advice = Advice.objects.get(pk=advice_id)

        serializer = AdviceSerializer(advice)
        return Response(serializer.data)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
