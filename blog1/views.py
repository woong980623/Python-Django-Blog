from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Profile, Category, Comment
from .forms import PostForm, ProfileForm, CommentForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    category_id = request.GET.get('category')
    if category_id:
        posts = Post.objects.filter(category_id=category_id).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    
    categories = Category.objects.all()
    return render(request, 'blog1/post_list.html', {'posts': posts, 'categories': categories})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog1/post_detail.html', {'post': post, 'comments': comments, 'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog1/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog1/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog1/post_confirm_delete.html', {'post': post})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'blog1/edit_profile.html', {'form': form})

@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'blog1/profile.html', {'profile': profile})
