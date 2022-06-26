from pyexpat.errors import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib import messages

from posts.forms import PostForm
from posts.models import Post


def viewPosts(request):
    posts = Post.objects.all()
    return render(request, "post/list.html", {'posts': posts})


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
            return redirect('dashboard')


class ViewUpdate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'

    model = Post
    form_class = PostForm
    template_name = 'post/edit.html'
    success_message = 'Post actualizado!!!'
    success_url = '/user/mis-posts/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user


class ViewDelete(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'

    model = Post
    template_name = 'post/delete.html'
    success_message = 'Post eliminado!!!'
    success_url = reverse_lazy('viewPosts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user
