from django.shortcuts import render
from .forms import NewPostForm
from .models import BlogPostModel
from django.http import HttpResponse


# load title page with link to new post
def index(request):
    posts = BlogPostModel.objects.all()
    return render(request, 'cwApp/index.html', {'posts': posts})

# make a new post
def newPost(request):
    makePost = NewPostForm()

    if request.method == 'POST':
        makePost = NewPostForm(request.POST)
        if makePost.is_valid():
            makePost.save(commit=True)
            return index(request)

    return render(request, 'cwApp/newPost.html', {'form': makePost})
