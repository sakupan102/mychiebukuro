from django.urls import path
from . import views

urlpatterns =[
    path("", views.top, name="top"),
    path("questions/", views.QuestionView.as_view(), name="questions"),
    path("questions/<int:pk>/", views.DetailView.as_view(), name ="detail"),
    path("questions/question_post/", views.question_post, name="question_post"),
    path("questions/<int:question_id>/answer_post/", views.answer_post, name="answer_post"),
    path("questions/post/<int:question_id>", views.question_result, name="question_result"),
    path("questions/<int:question_id>/answer_post/result", views.answer_result, name="answer_result"),
    path("questions/<int:question_id>/answer_post/post_to", views.answer_post_to, name="answer_post_to"),
    path("questions/question_post/post_to", views.question_post_to, name="question_post_to"),

]
