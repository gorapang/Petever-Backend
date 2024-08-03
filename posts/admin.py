from django.contrib import admin
from .models import Question, Letter, Answer, User

# admin.site.register(Question)
# admin.site.register(Letter)
# admin.site.register(Answer)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'date')
    search_fields = ('content', 'date')
    list_filter = ('date',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'content', 'created_at')
    search_fields = ('user__username', 'question__content', 'content')
    list_filter = ('created_at', 'user', 'question')

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'created_at')
    search_fields = ('user__username', 'content')
    list_filter = ('created_at', 'user')
