import rest_framework
from rest_framework.decorators import api_view, permission_classes
from .models import Comment
from rest_framework import views, viewsets
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from .serializers import CommentSerializer
from rest_framework import permissions
from random import randint
class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]


@api_view(http_method_names=["GET"])
@permission_classes([permissions.AllowAny])
def retrieve_random_comment(request):
    qs = Comment.objects.all()
    if qs.exists():
        count = qs.count()
        random_index = randint(0,count - 1)
        comment = CommentSerializer(qs[random_index])
        return Response(comment.data)
    return Response(None, status=200)


@api_view(http_method_names=["GET"])
@permission_classes([permissions.AllowAny])
def retrieve_random_comment_by_path(request, path: str):
    parsed_path = path.replace("%2F", "/")
    qs = Comment.objects.filter(path=parsed_path)
    print(parsed_path)
    if qs.exists():
        count = qs.count()
        random_index = randint(0,count - 1)
        comment = CommentSerializer(qs[random_index])
        return Response(comment.data)
    return Response(None, status=200)
