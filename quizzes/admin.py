from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from .models import Quiz, Question, QuizAttempt
from django import forms


# --- Custom form for QuestionInline ---
class QuestionInlineForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'option1': forms.TextInput(attrs={'style': 'width: 100%;'}),
            'option2': forms.TextInput(attrs={'style': 'width: 100%;'}),
            'option3': forms.TextInput(attrs={'style': 'width: 100%;'}),
            'option4': forms.TextInput(attrs={'style': 'width: 100%;'}),
        }

# --- Inline question editor inside Quiz ---
class QuestionInline(admin.TabularInline):
    model = Question
    form = QuestionInlineForm  # <-- assign custom form here
    extra = 1


# Quiz Admin
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'question_count', 'attempt_count', 'average_score')
    inlines = [QuestionInline]

    def question_count(self, obj):
        return obj.questions.count()
    question_count.short_description = 'Questions'

    def attempt_count(self, obj):
        return obj.quizattempt_set.count()
    attempt_count.short_description = 'Attempts'

    def average_score(self, obj):
        attempts = obj.quizattempt_set.all()
        if attempts.exists():
            return round(sum(a.score for a in attempts)/attempts.count(), 2)
        return 0
    average_score.short_description = 'Average Score'


# Question Admin
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'correct_answer')


# Custom Admin Site Dashboard
class QuizAdminSite(admin.AdminSite):
    site_header = "Quiz Manager"
    site_title = "Quiz Manager"
    index_title = "Dashboard"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('', self.admin_view(self.dashboard_view), name='index'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        quiz_count = Quiz.objects.count()
        question_count = Question.objects.count()

        # Quiz history: attempts per quiz
        quiz_attempts = []
        for quiz in Quiz.objects.all():
            attempts = quiz.quizattempt_set.all()
            total_attempts = attempts.count()
            avg_score = round(sum(a.score for a in attempts)/total_attempts, 2) if total_attempts else 0
            quiz_attempts.append({
                'title': quiz.title,
                'attempts': total_attempts,
                'average_score': avg_score,
            })

        context = {
            **self.each_context(request),
            "quiz_count": quiz_count,
            "question_count": question_count,
            "quiz_attempts": quiz_attempts,
        }
        return TemplateResponse(request, "admin/dashboard.html", context)


# Create custom admin site instance
quiz_admin_site = QuizAdminSite(name='quiz_admin')

# Register models to the custom admin site
quiz_admin_site.register(Quiz, QuizAdmin)
quiz_admin_site.register(Question, QuestionAdmin)
quiz_admin_site.register(QuizAttempt)
