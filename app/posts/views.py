from pyexpat.errors import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import model_to_dict
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib import messages

from posts.forms import PostForm, CommentForm
from posts.models import Post


def viewPosts(request):
    posts = Post.objects.all()
    return render(request, "post/list.html", {'posts': posts})


class ViewRead(DetailView):
    model = Post
    template_name = 'post/read.html'

    def get_context_data(self, **kwargs):
        context = super(ViewRead, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


def addComment(request):
    if request.method == 'POST':
        formComment = CommentForm(request.POST)
        if formComment.is_valid():
            instance = formComment.save(commit=False)
            instance.post_id = int(request.POST.get('post'))
            instance.save()
            return JsonResponse(model_to_dict(instance, fields=['person_name']), status=201)
        else:
            return JsonResponse(formComment.errors, safe=False, status=200)


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


class DeletePost(LoginRequiredMixin, View):
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'

    def post(self, request):
        post = Post.objects.get(pk=request.POST.get('post_id'))
        if post.user_id == request.user.id:
            post.delete()
            return JsonResponse({'delete': 'ok'}, status=201)
        else:
            return JsonResponse({}, safe=False, status=200)
