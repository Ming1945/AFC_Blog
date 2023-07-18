from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all() #to get all objectS from posts (database)
    posts = [post.to_dict() for post in posts]
    return render(request, 'index.html', {'posts' : posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    # posts = [post.to_dict() for post in posts]
    return render(request, 'posts.html', {'posts' : posts})

