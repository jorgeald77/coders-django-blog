from django.shortcuts import render


def dashboard(request):
    posts = request.user.posts.all()

    return render(request, 'dashboard.html', {
        'posts': posts,
        'author': request.user.profile.nombreCompleto()
    })
