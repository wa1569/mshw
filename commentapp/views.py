from .forms import CommentForm, PostForm
from .models import Post
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

# Create your views here.
# 기본 웹 페이지
def index(request):
    return render(request, 'commentapp/index.html')

def new(request):
    return render(request, 'commentapp/new.html')

# 글 작성 함수
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read')
    else:
        form = PostForm
        return render(request, 'commentapp/new.html', {'form':form})

# 글 불러오는 페이지
def read(request):
    posts = Post.objects
    return render(request, 'commentapp/read.html', {'posts':posts})

# 글 detail
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('detail', id)
    else:
        form = CommentForm()
        return render(request, 'commentapp/detail.html', {'post':post, 'form':form})