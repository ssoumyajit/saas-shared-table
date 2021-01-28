from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Post, Comments
from .serializers import (
    PostSerializer,
    CommentSerializer,
    UserSerializer,
)

from .utils import tenant_from_request

from django.contrib.auth import authenticate
from rest_framework.exceptions import PermissionDenied

from rest_framework.response import Response
from rest_framework import status


class PostViewSets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        """
        write the code for filtering our the dta specific to a single tenant.
        """
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)

    def destroy(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if not request.user == post.created_by:
            raise PermissionDenied("you can not delete this poll")
        return super().destroy(request, *args, **kwargs)


"""
class CommentsListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comments.objects.filter(post_id=self.kwargs["pk"])
        return queryset

    def post(self, request, *args, **kwargs):
        replied_by = request.data.get("replied_by")
        data = {""}
"""


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response(
                {"error": "wrong credentials"}, status=status.HTTP_400_BAD_REQUEST
            )



