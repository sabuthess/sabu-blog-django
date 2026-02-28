from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PostModel
from .forms import PostForm

def home(request): 
    posts = PostModel.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})

def create_post(request):
    form = PostForm()
    if(request.method == 'POST'):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'posts/create_post.html', {'form': form})

    

def view_post(request, id):
    post = PostModel.objects.get(id=id)
    return render(request, 'posts/post_view.html', {'post': post})



def update_post(request, id):
    post = PostModel.objects.get(id=id)
    form = PostForm(instance=post)
    if(request.method == 'POST'):
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'post_view', id=post.id)
    return render(request, 'posts/update_post.html', {
        'form': form,
        'post':post
        })



def delete_post(request, id):
    post = PostModel.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    return render(request, 'posts/delete_post.html', {'post': post})


