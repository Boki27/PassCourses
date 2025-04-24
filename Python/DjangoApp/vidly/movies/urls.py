# movies/urls.py
from django.urls import path
from . import views

app_name = 'movies'        # ← this enables the namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
]
