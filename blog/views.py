from django.shortcuts import HttpResponse, render, redirect

from blog.forms import PostForm
# Create your views here.
from blog.models import Post
from datetime import datetime


def create_post(request):
    if request.method == "GET":
        return render(request=request, template_name='form.html', context={'form': PostForm()})

    if request.method == "POST":
        Post.objects.create(title=request.POST.get("title"), author=request.POST.get("author"),
                            content=request.POST.get("content"), created_on=datetime.now(),
                            picture=request.FILES.get("picture"))
        return redirect('home')


def home(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request=request, template_name="home.html", context={'data': posts})


def post_edit(request, pk):
    if request.method == "GET":
        post = Post.objects.get(id=pk)
        form = PostForm(instance=post)
        return render(request=request, template_name="edit.html", context={'form': form})

    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.author = request.POST.get("author")
        post.picture = request.FILES.get("picture") if request.FILES.get("picture") else post.picture
        post.save()
        return redirect('home')


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request=request, template_name="detail.html", context={'post': post})


def post_delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('home')
