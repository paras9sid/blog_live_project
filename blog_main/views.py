from django.shortcuts import render
from blog_app.models import Blog
from assignments.models import About


def home(request):
    #fetch all categories defined dynamically in admin panel
    # categories = Category.objects.all() 
    #- commented above lines as context_processors used
    # print(categories)
    
    featured_posts = Blog.objects.filter(is_featured = True,status='Published')
    # print(featured_posts)
    
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-updated_at')
    # print(posts)
    
    #about us fetch    
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