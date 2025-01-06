from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BlogSerializer,TagSerializer,CategorySerializer
from .models import Blog
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, BasePermission
from .pagination import BlogPagination
from rest_framework.filters import OrderingFilter
from django.db.models import Q
from rest_framework.exceptions import NotFound
from rest_framework.authentication import TokenAuthentication
# Create your views here.
class IsOwner(BasePermission):
    def has_object_persmission(self,request, view ,obj):
        return obj.Author == request.user
    
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
    permission_classes = [IsOwner]
    
    def get_object(self, id):
        try:
            obj = Blog.objects.get(id=id)
            self.check_object_permissions(self.request, obj)
            return obj
        except Blog.DoesNotExist:
            raise NotFound("Blog not found")
        
    def put(self, request, *args, **kwargs):
        blog = self.get_object(kwargs['id'])
        serializer = BlogSerializer(blog, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)    
class BlogDeleteView(APIView):
    permission_classes = [IsOwner | IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get_object(self, id):
        try:
            obj = Blog.objects.get(id=id)
            self.check_object_permissions(self.request, obj)
            return obj
        except Blog.DoesNotExist:
            raise NotFound("Blog not found")

    def delete(self, request, *args, **kwargs):
        blog = self.get_object(kwargs['id'])
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
class BlogFilterationView(APIView):
    def get(self,request,*args,**kwargs) :
        category=request.query_params.get('Category','')
        author=request.query_params.get('Author','')
        blogs=Blog.objects.filter(Q(Category__name=category)|Q(Author__username=author)) 
        serializer=BlogSerializer(blogs,many=True) 
        return Response(serializer.data,status=200)    
class BlogListView(APIView):
    pagination_class = BlogPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['Published_Date','Category']
    
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.filter(Published_Date__isnull=False).all()
        paginator =  self.pagination_class()
        sort_by = request.query_params.get('sort','')
        if sort_by:
            blogs = blogs.order_by(sort_by)
        page = paginator.paginate_queryset(blogs, request, view=self)
        if page is not None:
            serializer = BlogSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=200)     
    