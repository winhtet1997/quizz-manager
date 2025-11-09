from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, QuizAttempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()  # no need for prefetch_choices
    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz, 'questions': questions})

def quiz_submit(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method != 'POST':
        return redirect('quizzes:detail', pk=pk)

    questions = quiz.questions.all()
    correct = 0
    total = questions.count()

    for q in questions:
        selected = request.POST.get(f'question_{q.id}')
        if not selected:
            continue
        # Compare selected option (A/B/C/D) with correct_answer
        if selected == q.correct_answer:
            correct += 1

    # save attempt
    attempt = QuizAttempt.objects.create(
        quiz=quiz,
        user=request.user if request.user.is_authenticated else None,
        score=correct,
        total=total
    )

    messages.success(request, f'You scored {correct}/{total}')
    return render(request, 'quizzes/result.html', {
        'quiz': quiz,
        'score': correct,
        'total': total,
        'attempt': attempt
    })

@login_required
def history(request):
    attempts = QuizAttempt.objects.filter(user=request.user).order_by('-taken_at')
    return render(request, 'quizzes/history.html', {'attempts': attempts})
