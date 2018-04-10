from math import ceil
from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title,content=content)
        return redirect('/post/read/?post_id=%s' % post.id)
    return render(request,'create_post.html',{})

def edit_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/post/read/?post_id=%s' % post.id)
    else:
        post_id = int(request.GET.get('post_id'))
        post = Post.objects.get(id=post_id)
        return render(request,'edit_post.html',{'post':post})

def read_post(request):
    post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(id=post_id)
    return render(request,'read_post.html',{'post':post})

def list_post(request):
    total = Post.objects.all().count()  # 文章总数

    pages = ceil(total/5) #总页数
    page = int(request.GET.get('page', 1))  # 默认第一页
    start = (page-1)*5
    end = start+5
    posts = Post.objects.all()[start:end]
    # 分页按钮显示
    return render(request,'post_list.html',{'posts':posts,'pages':range(1,pages+1)})
