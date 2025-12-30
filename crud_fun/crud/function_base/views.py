from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def fbv_api_list(request):
    if request.method == "GET":
       posts = Post.objects.all()
       serializer = PostSerializer(posts, many=True)
       return Response(serializer.data)
    
    if request.method == "POST":
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)


@api_view(['GET', 'Put','DELETE'])
def fbv_post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(
            {"error": f"Post with id {pk} not found"},
            status=404
        )
    
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    if request.method == "PUT":
        return Response(PostSerializer(post))
    
    if request.method == "DELETE":
        post.delete()
        return Response({"message": "Deleted"}, status=204)

    

