from django.shortcuts import render

from myapp2.models import Player
from rest_framework.viewsets import ModelViewSet

from myapp2.serializers import PlayerSerializer


def index_page(request):
    all_players = Player.objects.all()
    print(all_players)
    # good_players = Player.objects.filter(number=92)
    # print(good_players)
    # new_player = Player(name='Pellegrini', number=7)
    # new_player.save()
    # pl = Player.objects.get(id=7)
    # pl.delete()
    # pl.save()
    return render(request, 'index.html', {'players': all_players})


class PlayerView(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


def players_page(request):
    return render(request, 'players.html')
