from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDict

from blog.forms import PostForm
from blog.models import Post


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(
        request=request,
        template_name='form.html',
        context={'form': form, 'title': 'Crear Post'}
    )


def home(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request=request, template_name="home.html", context={'data': posts})


def post_edit(request, pk):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post.title = request.POST.get("title")
            post.content = request.POST.get("content")
            post.author = request.POST.get("author")
            post.picture = request.FILES.get("picture") or post.picture
            post.save()
            return redirect('home')
    else:
        post = Post.objects.get(id=pk)
        form = PostForm(instance=post)
    return render(request=request, template_name="form.html", context={'form': form, 'title': 'Editar Post'})


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request=request, template_name="detail.html", context={'post': post})


def post_delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('home')
