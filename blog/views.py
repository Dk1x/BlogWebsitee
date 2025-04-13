from django.shortcuts import render, get_object_or_404
from .models import Comment, Post, Category,User

def main(request):
    return render(request, 'blog/main.html')

def users_view(request):
    users = User.objects.all()
    return render(request, 'blog/users.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'blog/user_detail.html', {'user': user})

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/category_detail.html', {'category': category})

def comments_view(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comments.html', {'comments': comments})

def blogdetails(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/blogdetails.html', {'post': post})

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blogs.html', {'posts': posts})