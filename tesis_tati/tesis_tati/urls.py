"""tesis_tati URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from comments.views import CommentViewSet, RandomCommentsByPath, retrieve_random_comment_by_path, retrieve_random_comment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("server/admin/", admin.site.urls),
    path("server/api/", include(router.urls)),
    path("server/api/random-comment-by-path/<str:path>/", retrieve_random_comment_by_path),
    path("server/api/random-comments-by-path/<str:path>/", RandomCommentsByPath.as_view({'get': 'list'})),
    path("server/api/random-comment/", retrieve_random_comment),
]
urlpatterns += staticfiles_urlpatterns()
