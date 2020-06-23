from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=50)
    question_answer = models.CharField(max_length=50)
    human_answer = models.CharField(max_length=50, default='', blank=True)

    def check_answers(self):
        if self.question_answer.lower() == self.human_answer.lower():
            return 'Верно'
        else:
            return 'Неверно'