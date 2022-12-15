from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm


def start(request):
    return render(request, 'blog/start.html')


def index(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'blog/index.html', {'title': 'Головна сторінка', 'posts': posts})


def about(request):
    return render(request, 'blog/about.html')


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = PostForm()
    context = {
        'form': form
    }

    return render(request, 'blog/create_post.html', context)


def index_tab(request):
    posts = Post.objects.all()
    return render(request, 'blog/index_tab.html', {'title': 'Перелік постів', 'posts': posts})


def post_view(request, id=1):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_view.html', {'title': 'Обраний пост', 'post': post})


def post_edit(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = PostForm()
        else:
            post = get_object_or_404(Post, id=id)
            form = PostForm(instance=post)

        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        if id == 0:
            form = PostForm(request.POST)
        else:
            post = get_object_or_404(Post, id=id)
            form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

        return redirect('blog')


def post_delete(request, id=0):
    post = get_object_or_404(Post, id=id)
    post.delete()

    posts = Post.objects.all()

    return render(request, 'blog/index_tab.html', {'title': 'Перелік постів', 'posts': posts})
