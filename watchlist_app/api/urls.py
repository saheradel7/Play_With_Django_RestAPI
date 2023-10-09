from django.urls import path
#from .views import movie_list ,movie_detail 
from .views import MovieList,MovieDetail
urlpatterns = [
    # path('list/' , movie_list , name='MovieList'),
    # path('list/<int:pk>/' , movie_detail , name='Movied')
    path('list/' , MovieList.as_view() , name='Movie'),
    path('list/<int:id>' , MovieDetail.as_view() , name='MovieDetail'),
]
