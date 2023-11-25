from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password

from core.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "name", "is_avaliador", "is_professor", "is_aluno")

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)
