from myapp2.models import Player
from rest_framework.serializers import ModelSerializer


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['name', 'number']