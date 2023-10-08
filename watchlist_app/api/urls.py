from django.urls import path
from .views import movie_list ,movie_detail

urlpatterns = [
    path('list/' , movie_list , name='MovieList'),
    path('list/<int:pk>/' , movie_detail , name='Movied')
]
