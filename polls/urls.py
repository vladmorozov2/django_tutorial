from django.urls import path
from . import views

app_name = "polls12"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail123"),
    path("<int:question_id>/results/", views.results, name="result123"),
    path("<int:question_id>/vote/", views.vote, name="vote123"),
]
