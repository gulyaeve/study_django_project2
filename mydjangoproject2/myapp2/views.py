from django.shortcuts import render

from myapp2.models import Player


def index_page(request):
    all_players = Player.objects.all()
    print(all_players)
    # good_players = Player.objects.filter(number=92)
    # print(good_players)
    # new_player = Player(name='Pellegrini', number=7)
    # new_player.save()
    pl = Player.objects.get(id=7)
    pl.delete()
    # pl.save()
    return render(request, 'index.html')
