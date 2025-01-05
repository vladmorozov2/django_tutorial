from django.urls import path
from . import views

app_name = "polls12"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail123"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="result123"),
    path("<int:question_id>/vote/", views.vote, name="vote123"),
]
