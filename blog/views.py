from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BlogSerializer,TagSerializer,CategorySerializer
from .models import Blog
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Q


# Create your views here.
class BlogViewCreation(APIView):
    def post(self , request,*args, **kwargs):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
class BlogDetailsView(APIView):
    def get(self, request, *args,**kwargs):
        blog = Blog.objects.get(id=kwargs['id'])
        serializer =BlogSerializer(blog)
        return Response(serializer.data,status=200)


class BlogUpdateView(APIView):
    def put(self, request,*args,**kwargs):
        blog=Blog.objects.get(id=kwargs['id'])
        serializer=BlogSerializer(blog,partial=True,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors,status=400)
class BlogDeleteView(APIView):
    def delete(self,requests,*args,**kwargs):
        blog=Blog.objects.get(id=kwargs['id'])
        blog.delete()
        return Response(status=204)   
class TagCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201) 
        return Response(serializer.errors,status=400)
class CategoryCreationView(APIView):
    permission_classes=[IsAdminUser]
    def post(self,request,*args,**kwargs):
        serializer=CategorySerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201) 
        return Response(serializer.errors,status=400)      
class SearchView(APIView):
        def get(self,request,*args,**kwargs):
            query=request.query_params.get('q','')
            blogs=Blog.objects.filter(Q(Title__icontains=query)|Q(Content__icontains=query)|Q(Author__username__icontains=query)|
                                      Q(tag__name__icontains=query))
            serializer =BlogSerializer(blogs,many=True) 
            return Response(serializer.data,status=200)   