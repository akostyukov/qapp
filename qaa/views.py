from django.shortcuts import render, redirect
from django.views import generic

from .models import Question


class IndexView(generic.ListView):
    model = Question
    template_name = 'qaa/index.html'
    context_object_name = 'list_of_questions'


def create(request):
    Question.objects.create(
        question_text=request.POST['question'],
        question_answer=request.POST['answer']
    )
    return redirect('qaa:index')

def edit(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == 'GET':
        return render(request, 'qaa/edit.html', {'question': question})
    else:
        question.question_text = request.POST['question']
        question.question_answer = request.POST['answer']
        question.save()
        return redirect('qaa:index')

def delete(request, question_id):
    Question.objects.get(id=question_id).delete()
    return redirect('qaa:index')

def start(request):
    questions = Question.objects.all()
    questions_with_answer = []
    question_without_answer = None
    count_of_correct_answers = 0
    
    for q in questions:
        if q.human_answer:
            questions_with_answer.append(q)  
        else:
            question_without_answer = q
            break 

    for question in questions_with_answer:
        if question.human_answer == question.question_answer:
            count_of_correct_answers += 1

    return render(request, 'qaa/start.html', {
        'questions_with_answer': questions_with_answer,
        'question_without_answer': question_without_answer,
        'count_of_correct_answers': count_of_correct_answers,
        'count_of_answers': f'{len(questions)} ({100 // len(questions) * count_of_correct_answers}%)'
    })

def add_answer(request, question_id):
    question = Question.objects.get(id=question_id)

    if question.question_answer.lower() == request.POST['human_answer'].lower():
        question.human_answer = question.question_answer
    else:
        question.human_answer = request.POST['human_answer']
        
    question.save()
    return redirect('qaa:start')

def clear(request):
    Question.objects.all().delete()
    return redirect('qaa:index')
