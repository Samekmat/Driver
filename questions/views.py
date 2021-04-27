from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer


class QuestionListView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionView(APIView):
    def get(self, request, question_id):
        question = Question.objects.get(pk=question_id)

        serializer = QuestionSerializer(question)
        return Response(serializer.data)
