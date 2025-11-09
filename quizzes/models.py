from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def question_count(self):
        return self.questions.count()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=300)
    option1 = models.CharField(max_length=100, default='Option 1')
    option2 = models.CharField(max_length=100, default='Option 2')
    option3 = models.CharField(max_length=100, default='Option 3')
    option4 = models.CharField(max_length=100, default='Option 4')

    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Option 1'),
            ('B', 'Option 2'),
            ('C', 'Option 3'),
            ('D', 'Option 4'),
        ],
        default='A',
    )

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    total = models.PositiveIntegerField(default=0)  # ✅ new field
    taken_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} ({self.score}/{self.total})"

