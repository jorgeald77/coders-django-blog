from pyexpat.errors import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib import messages

from posts.forms import PostForm
from posts.models import Post


def viewPosts(request):
    posts = Post.objects.all()
    return render(request, "post/list.html", {'posts': posts})


# TODO Hacer uso de MessageMixin
class ViewCreate(LoginRequiredMixin, View):
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = PostForm()
        return render(request, 'post/create.html', {"form": form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            blogPost = form.save(commit=False)
            blogPost.user = request.user
            blogPost.save()
            messages.success(request, f'El post "{blogPost.title}", se ha guardado.')
            return redirect('viewPosts')


# TODO Hacer uso de UserPassesTestMixin y MessagesMixin
class ViewUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'

    model = Post
    form_class = PostForm
    template_name = 'post/edit.html'


# TODO Hacer uso de UserPassesTestMixin y  MessagesMixin
class ViewDelete(LoginRequiredMixin, DeleteView):
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'

    model = Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('viewPosts')
