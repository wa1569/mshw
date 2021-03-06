from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm

#메인페이지
def main(request):
    posts = Post.objects
    return render(request, 'blog/main.html', {'posts':posts})

#글쓰기페이지
def write(request):
    return render(request, 'blog/create.html')

#글쓰기 함수
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form= form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read')

    else:
        form=PostForm
        return render(request, 'blog/write.html', {'form':form})

#읽기페이지
def read(request):
    posts = Post.objects
    return render(request, 'blog/read.html', {'posts':posts})

#디테일페이지
def detail(request, id):
    post = get_object_or_404(Post, id = id)
    return render(request, 'blog/detail.html', {'post':post})

#수정페이지
def edit(request):
    return render(request, 'blog/edit.html')

#수정 함수
def edit(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method =="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')
        
    else:
        form= PostForm(instance=post)
        return render(request, 'blog/edit.html', {'form':form})


def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('read')