from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Post, Tag

# Create your views here.
def index(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    display="none"
    context={"posts": posts, "display": display, "tags": tags}
    return render(request, "index.html", context)

def search(request):
    tag_title = request.GET.get("search")
    tags = {}
    if tag_title != "":
        if Tag.objects.filter(title__icontains=tag_title).exists():
            tags = Tag.objects.all()
    display="block"
    context = {"tags": tags, "display": display}
    return render(request, "suggestions.html", context)


def append_tag(request,pk):
    tag = Tag.objects.get(id=pk)
    title = tag.title
    posts = Post.objects.filter(tags__title__icontains=title)
    context={"title": title, "posts": posts}
    return render(request, "index.html", context)


def form_search(request):
    title = request.GET.get("search")
    posts = {}
    msg = ""
    if title != "":
        posts = Post.objects.filter(Q(tags__title__icontains=title) | Q(title__icontains=title) | 
                                    Q(description__icontains=title)).distinct()
        if posts.exists():
            pass
            
        
        else:
            msg = "There is no post with given keyword"
    
    context = {"title": title, "msg":msg, "posts": posts}
    return render(request, "index.html", context)
    
        
        