from django.shortcuts import render
from .models import *


def index(request):
    films = Film.objects.all()
    films_info = []
    for film in films:
        film_info = {'title': film.title}
        filmgenres = film.filmgenre_set.all()
        genres = []
        for filmgenre in filmgenres:
            genres.append(filmgenre.genre.name)
        film_info['genres'] = ', '.join(genres)
        film_info['poster'] = film.poster.url
        sessions = film.session_set.all()
        rooms = Room.objects.filter(session__in=sessions).distinct()
        film_info['rooms'] = []
        for room in rooms:
            room_info = {'name': room.name}
            room_sessions_times = []
            room_sessions_prices = []
            room_sessions = sessions.filter(room=room)
            for room_session in room_sessions:
                room_sessions_times.append(str(room_session.time)[:5])
                room_sessions_prices.append(str(room_session.price))
            room_info['times'] = room_sessions_times
            room_info['prices'] = room_sessions_prices
            film_info['rooms'].append(room_info)
        films_info.append(film_info)
    return render(request, 'Main/Index.html', {'films_info': films_info})
