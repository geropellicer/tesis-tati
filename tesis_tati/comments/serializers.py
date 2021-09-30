from users.models import Usuario
from .models import Comment
from users.serializers import UsuarioSerializer
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(many=False)

    class Meta:
        model = Comment
        fields = ["user", "text"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user, created = Usuario.objects.get_or_create(email=user_data["email"], defaults={"nombre": user_data["nombre"], "apellido": user_data["apellido"]})

        comment = Comment.objects.create(user=user, text=validated_data["text"])

        return comment

