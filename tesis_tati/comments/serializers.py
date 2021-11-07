from users.models import Usuario
from .models import Comment
from users.serializers import UsuarioSerializer
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(many=False)

    class Meta:
        model = Comment
        fields = ["id", "path", "user", "text", "created_at", "updated_at"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user, created = Usuario.objects.get_or_create(nombre=user_data["nombre"])

        comment = Comment.objects.create(user=user, text=validated_data["text"], path=validated_data["path"])

        return comment
