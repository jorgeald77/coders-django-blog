from django.shortcuts import render


def dashboard(request):
    # TODO Obtener los posts creados por el usuario autenticado  desde la DB
    posts = [
        {'id': 1, 'title': 'lorem10', 'published': '2022-05-10'},
        {'id': 1, 'title': 'lorem10', 'published': '2022-05-10'},
    ]

    return render(request, 'dashboard.html', {
        'posts': posts,
        'author': request.user.profile.nombreCompleto()
    })
