from pyexpat.errors import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView, CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from posts.forms import PostForm, CommentForm
from posts.models import Post, Comment

def viewPosts(request):
    posts = Post.objects.all()

    return render(request, "post/viewposts.html", {'posts': posts})


class ReadPost(DetailView):
    model = Post
    template_name = 'post/enterpost.html'

class ViewCreate(LoginRequiredMixin, View):
    login_url =  '/auth/login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = PostForm()
        return render(request, 'post/postform.html', {"form": form})

    def post(self, request):

        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():

            blogPost = form.save(commit=False)
            
            blogPost.user =  request.user
            
            blogPost.save()


            messages.success(request, f'El post "{blogPost.title}", se ha guardado.')
            
            return redirect('viewPosts')


class ViewUpdate(LoginRequiredMixin, UpdateView):
    login_url =  '/auth/login'
    redirect_field_name = 'redirect_to'

    model = Post
    form_class = PostForm
    template_name = 'post/updatepostform.html'


class ViewDelete(LoginRequiredMixin, DeleteView):
     login_url =  '/auth/login'
     redirect_field_name = 'redirect_to'

     model = Post
     template_name = 'post/viewposts.html'
     success_url = reverse_lazy('viewPosts')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/addcomment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('viewPosts')
