from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Question, Letter, Answer, User
from .serializers import QuestionSerializer, AnswerSerializer, LetterSerializer
from itertools import chain
from operator import attrgetter
import datetime


class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionListView(generics.ListAPIView):

    serializer_class = QuestionSerializer

    def get_queryset(self):
        date_str = self.kwargs.get('date')
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            raise QuestionSerializer.ValidationError({"error": "Invalid date format. Use YYYY-MM-DD."})

        return Question.objects.filter(date=date_obj)
    

class LetterView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        letters = Letter.objects.filter(user=request.user).order_by('-created_at')
        serializer = LetterSerializer(letters, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = LetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        answers = Answer.objects.filter(user=request.user).order_by('-created_at')
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListAllPostsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        answers = Answer.objects.filter(user=request.user)
        letters = Letter.objects.filter(user=request.user)

        combined = sorted(
            chain(answers, letters),
            key=attrgetter('created_at'),
            reverse=True
        )

        response_data = []
        for item in combined:
            if isinstance(item, Answer):
                serializer = AnswerSerializer(item)
                response_data.append({'type': 'answer', **serializer.data})
            elif isinstance(item, Letter):
                serializer = LetterSerializer(item)
                response_data.append({'type': 'letter', **serializer.data})

        return Response(response_data)


class DetailAnswerView(APIView):
    def get(self, request, *args, **kwargs):
        answer = get_object_or_404(Answer, pk=kwargs.get('pk'))
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

class DetailLetterView(APIView):
    def get(self, request, *args, **kwargs):
        letter = get_object_or_404(Letter, pk=kwargs.get('pk'))
        serializer = LetterSerializer(letter)
        return Response(serializer.data)
    