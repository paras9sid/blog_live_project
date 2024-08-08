from django.shortcuts import render
from blog_app.models import Blog
from assignments.models import About


def home(request):
    
    featured_posts = Blog.objects.filter(is_featured = True,status='Published')
    # print(featured_posts)
    
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-updated_at')
    # print(posts)
    
    #about us fetch    - get will fetch only 1 single data and try will only work with get
    try:
        about = About.objects.get()
    except:
        about = None
    
    context = {
        # 'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
        'about':about,
    }
    return render(request,'home.html',context)