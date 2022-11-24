from django.shortcuts import render,redirect
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from home.decorators import check_profile
from django.core.paginator import Paginator

# Create your views here.
def blog_index(request):
    form = PostForm()
    post_list = Post.objects.all().order_by('-created_on')
    paginator = Paginator(post_list,8)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        'posts':posts,
        'form':form,
    }
    return render(request, 'blog/index.html',context)

@login_required
@check_profile
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
    comment_form = CommentForm()
    comments = post.comment_set.all()
    print(comments)
    context = {
        'post':post,
        'form':form,
        'c_form': comment_form,
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

@login_required
@check_profile
def create_comment(request,id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user.alumni_profile
            new_comment.post = Post.objects.get(id=id)
            new_comment.save()
            form.save_m2m()
            return redirect('blog:post_details', id)

def edit_comment(request,id):
    comment = Comment.objects.get(id=id)
    new_body = request.POST['comment']
    comment.body = new_body
    comment.save()
    return redirect('blog:post_details',comment.post.id)

def delete_comment(request,id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('blog:post_details',comment.post.id)
