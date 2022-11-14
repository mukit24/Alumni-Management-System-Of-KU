from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post
# Create your views here.
def blog_index(request):
    form = PostForm()
    posts = Post.objects.all()
    context = {
        'posts':posts,
        'form':form,
    }
    return render(request, 'blog/index.html',context)

def create_post(reqeust):
    if reqeust.method == 'POST':
        form = PostForm(reqeust.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = reqeust.user.alumni_profile
            new_post.save()
            form.save_m2m()
            return redirect('blog:blog_index')

def post_detials(request,id):
    post = Post.objects.get(id=id)
    form = PostForm(instance = post)
    context = {
        'post':post,
        'form':form,
    }
    return render(request,'blog/detail.html',context)

def edit_post(request,id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog:post_details',post.id)

def delete_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('blog:blog_index')
