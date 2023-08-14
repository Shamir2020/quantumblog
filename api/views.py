from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pages.models import *
from api.serializers import BlogSerializer
# Create your views here.
@api_view(['GET'])
def getFeaturedBlogs(request):
    response = {'status':200}
    blogs = Blog.objects.filter(featured=True)
    serializer = BlogSerializer(blogs,many=True)

    response['data'] = serializer.data

    return Response(response)

@api_view(['GET'])
def getAllBlogs(request):
    response = {'status':200}
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs,many=True)

    response['data'] = serializer.data 

    return Response(response)