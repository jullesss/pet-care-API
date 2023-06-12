"""
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=15)
    last_name = serializers.CharField(max_length=15)
    email = serializers.EmailField()

    # auto_now_add -> Atualização no momento de criação do dado
    created_at = serializers.DateTimeField(read_only=True)
    # auto_now -> Atualização no momento de atualização do dado
    updated_at = serializers.DateTimeField(read_only=True)

    recipes = RecipeSerializer(many=True, read_only=True)
"""

from rest_framework import serializers
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.CharField()

    group = GroupSerializer()
    traits = TraitSerializer(many=True)
