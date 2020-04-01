from django.urls import path
from . import views


# the polls app has a detail view, and so might an app on the same project that
#  is for a blog. How does one make it so that Django knows which app view to 
#  create for a url when using the {% url %} template tag?
#  Now change your polls/index.html template to specify that it is calling 
#  detal view of polls app.
app_name = 'polls'
# urlpatterns = [

#     # ex: /polls/
#     path('', views.index,name='index'),
#     # ex: /polls/5/
#     path('<int:q>/', views.detail, name='detail'), #'q' i.e. the name of variable should be same as the parameter
#     											   # being passed in the function 'detail()'
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]