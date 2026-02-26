from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def create_post(request):
    form = PostForm()
    return render(request, 'create_posts.html', {'form': form})


def update_post(request):
    return 

def delete_post(request):
    return 

def view_post(request):
    return 

