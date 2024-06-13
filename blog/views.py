from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment, SiteSettings, Page
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm, CategoryForm, CommentForm
from django.conf import settings
import requests

def get_latest_posts_and_comments():
    latest_posts = Post.objects.order_by('-post_time')[:5]
    latest_comments = Comment.objects.filter(active=True).order_by('-created_on')[:5]
    return latest_posts, latest_comments

def post_list(request):
    posts = Post.objects.order_by('-post_time')
    site_settings = SiteSettings.objects.first()
    posts_per_page = site_settings.posts_per_page if site_settings else 5

    paginator = Paginator(posts, posts_per_page)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    latest_posts, latest_comments = get_latest_posts_and_comments()

    return render(request, 'post_list.html', {
        'posts': posts,
        'latest_posts': latest_posts,
        'latest_comments': latest_comments
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_submitted = False

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.ip_address = request.META['REMOTE_ADDR']

            if Comment.objects.filter(email=new_comment.email, name=new_comment.name, active=True).exists():
                new_comment.active = True
            else:
                new_comment.active = False

            new_comment.save()
            comment_submitted = True
    else:
        comment_form = CommentForm()

    latest_posts, latest_comments = get_latest_posts_and_comments()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comment_submitted': comment_submitted,
        'latest_posts': latest_posts,
        'latest_comments': latest_comments
    })

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_edit.html', {'form': form})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_edit.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page_detail.html', {'page': page})
