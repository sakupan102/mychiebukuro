from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from django.urls import reverse
from django.views import generic
from django.utils import timezone



def top(request):
    return render(request, "situmon/top.html",)


class QuestionView(generic.ListView):
    model = Question
    template_name = "situmon/questions.html"
    paginate_by =10



class DetailView(generic.DetailView):
    model = Question
    template_name = "situmon/detail.html"

def  question_post(request):
    return HttpResponse("質問を投稿する場所です(制作途中)")

def answer_post(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    context = {"question": question}
    return render(request, "situmon/answer_post.html", context)
def answer_result(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    context={"question":question}
    return render(request,"situmon/answer_result.html", context)

def question_result(request, question_id):
    return HttpResponse("投稿した質問を表示します")

def answer_post_to(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        answer_txt=request.POST["answer_text"]
    except (KeyError):
        return render(
            request,
            "situmon/answer_post.html",
            {
                "question": question,
                "error_message": "回答がありません!!"
            }
        )
    else:
        question.answer_set.create(answer_text=answer_txt, pub_date=timezone.now())
        return HttpResponseRedirect(reverse("answer_result", args=(question.id,)))



def question_post_to(request):
    return HttpResponse("フォームから情報を受け取って、結果ページにリダイレクトする")
