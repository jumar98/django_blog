from django.shortcuts import HttpResponse, render
from blog.forms import PostForm
# Create your views here.


def hello_world(request):
    return render(request=request, template_name='form.html', context={'form': PostForm()})
