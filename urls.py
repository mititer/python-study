from django.urls import path

def detail():
    return True

app_name = 'polls'
urlpatterns = [
    path('', detail, name='index'),
    # ex: /pools/5
    path('<int:question_id>/', detail, name="detail"),
    # ex: /pools/5/results
    path('<int:question_id>/results/', detail, name="results"),
    # ex: /pools/5/vote
    path('<int:question_id>/vote/', detail, name="vote"),
    ]