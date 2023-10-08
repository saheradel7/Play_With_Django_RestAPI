# from django.shortcuts import render
# from .models import Movie
# from django.http import HttpResponse
# from django.http import JsonResponse
# # Create your views here.

# def movie_list(request ):
#     movies = Movie.objects.all()
#     # data = {'movie' : list(movies.values())}
#     # return JsonResponse(data)
#     print("\\\\\=========>" , movies,"<===========/////")
#     data = movies.values()
#     return JsonResponse(data[0])


# def movie_detail(request,pk ):
#     movies = Movie.objects.get(pk = pk)
#     data = {
#         'name': movies.name,
#         'description': movies.description,
#         'active' : movies.active
#     }
#     print("\\\\\=========>" ,data,"<===========/////")
#     return JsonResponse(data)

