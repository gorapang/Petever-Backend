from django.urls import path
from .views import LetterView, AnswerView, ListAllPostsView, DetailLetterView, DetailAnswerView, QuestionCreateView, QuestionListView
# CreateLetterView, CreateAnswerView,
urlpatterns = [
    
    path('letter/', LetterView.as_view(), name='list_letters'),
    path('answer/', AnswerView.as_view(), name='list_answers'),
    path('allposts/', ListAllPostsView.as_view(), name='list_all_posts'),

    path('letter/<int:pk>/', DetailLetterView.as_view(), name='letter_detail'),
    path('answer/<int:pk>/', DetailAnswerView.as_view(), name='answer_detail'),

    path('question/<str:date>/', QuestionListView.as_view(), name='question_detail'),
    path('question/', QuestionCreateView.as_view(), name='question_detail'),
]