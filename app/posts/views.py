from django.shortcuts import render
from django.forms.models import model_to_dict
from posts.models import BlogPost
from posts.forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
def blogPostForm(request): #para agregar nuevos posteos
    
    if request.method == 'POST':

        form = PostForm(request.POST)
        
        print(form)

        if form.is_valid:

            info = form.cleaned_data

            blogPost = BlogPost(titulo=info['titulo'], contenido=info['contenido'], fecha=info['fecha'])

            blogPost.save()

            return render(request, 'post/postadded.html')

    else:

        form = PostForm()

    return render(request, 'post/postform.html', {"form":form})


def viewPosts(request):

    posts = BlogPost.objects.all()

    context = {"posts": posts}

    return render(request, "post/viewposts.html", context)


def updatePosts(request, pk: int):

    blogpost = BlogPost.objects.get(pk=pk)

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            blogpost.titulo = info['titulo']
            blogpost.contenido = info['contenido']
            blogpost.fecha = info['fecha']

            blogpost.save()

            blogpost = BlogPost.objects.all()
            context = {
                'blogpost': blogpost
            }

            return render(
                request=request,
                context=context,
                template_name='post/viewposts.html'
            )

    form = PostForm(model_to_dict(blogpost))
    context = {
        'blogpost':blogpost,
        'form':form,
    }
    return render(
        request=request,
        context=context,
        template_name='post/updatepostform.html'
    )

def deletePosts(request, pk: int):

    blogpost = BlogPost.objects.get(pk=pk)
    if request.method == 'POST':
        blogpost.delete()

        blogposts = BlogPost.objects.all()

        context = {"blogpost":blogpost}

        return render(
            request=request,
            context=context,
            template_name="post/viewposts.html")
    context = {
        'blogpost':blogpost
    }
    return render(
        request=request,
        context=context,
        template_name='post/postconfirmdelete.html'
    )

    #recordar trabajar en la rama dedicada para esto