from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    # ex: /forms/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /forms/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /forms/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /forms/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),]
