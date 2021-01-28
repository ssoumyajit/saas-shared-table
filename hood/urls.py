from django.urls import path
from .apiviews import PostViewSets, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register("posts", PostViewSets)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("users/", UserCreate.as_view(), name="user_create"),
    # path("posts/<int:pk>/comments/", CommentsListCreateView.as_view(), name="comments"),
]

urlpatterns += router.urls
