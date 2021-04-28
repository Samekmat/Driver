from rest_framework import serializers
from .models import Question, Training, Answer, Category, Advice


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'url', 'content')


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'url', 'content', 'is_correct', 'question')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'name')


class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = ('id', 'url', 'name', 'multimedia', 'content', 'training', 'category')
