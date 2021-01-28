from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Post


def posts_list(request):
    max_objects = 20
    posts = Post.objects.all()[:20]
    data = {
        "results": list(
            posts.values("pk", "posts", "created_by")
        )
    }
    return JsonResponse(data)


def posts_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        "results": {
            "post": post.post,
            "created_by": post.created_by,
        }
    }
    return JsonResponse(data)
