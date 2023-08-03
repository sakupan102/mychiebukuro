from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField("date published")
    question_title = models.CharField(max_length=100)
    def __str__(self):
        return self.question_title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    pub_date=models.DateTimeField("date published")
    def __str__(self):
        ans = self.answer_text[:10]+"..."
        return ans

