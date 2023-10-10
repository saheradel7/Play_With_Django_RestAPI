from watchlist_app.models import Movie
from . serializer import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# region functionbasedView

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many =True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=201)


# @api_view(['GET', 'PUT' , 'DELETE'])
# def movie_detail(request,pk):
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk = pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk = pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=400)
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk = pk)
#         movie.delete()
#         return Response(status=204)
# endregion


class MovieList(APIView):
    def get(self,request):
        movies= Movie.objects.all()
        serializer = MovieSerializer(movies,many = True)
        return Response(serializer.data , status = status.HTTP_200_OK )
        
    def post(self,request):
        serializer = MovieSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response( serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    
class MovieDetail(APIView):
    def get(self, request , id):
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data , status = status.HTTP_200_OK)
    
    def put(self ,request , id):
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)
        return Response(serializer.errors  , status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request, id):
        movie = Movie.objects.get(id=id)
        movie.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
