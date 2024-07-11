from django.shortcuts import get_object_or_404, render,redirect
from blog_app.models import Category,Blog
from django.http import HttpResponse


def home(request):
    
    #fetch all categories defined dynamically in admin panel
    categories = Category.objects.all()
    # print(categories)
    
    featured_posts = Blog.objects.filter(is_featured = True,status='Published')
    # print(featured_posts)
    
    posts = Blog.objects.filter(is_featured=False).order_by('-updated_at')

    posts = Blog.objects.filter(is_featured=False ,status='Published').order_by('-updated_at')
    # print(posts)
    
    
    context = {
        # 'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
    }
    return render(request,'home.html',context)