from django.shortcuts import get_object_or_404, render,redirect

from assignments.models import About

from .models import  Category,Blog
from django.http import HttpResponse

def home(request):
    #fetch all categories defined dynamically in admin panel
    # categories = Category.objects.all() 
    #- commented above lines as context_processors used
    # print(categories)
    
    featured_posts = Blog.objects.filter(is_featured = True,status='Published')
    # print(featured_posts)
    
    posts = Blog.objects.filter(is_featured=False).order_by('-updated_at')
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

def posts_by_category(request,pk):
    # print(pk) # working checked 
    # return HttpResponse('<h2>Posts by category!!</h2>') # working checked
    
    # fetch the post belong to id/pk of category
    posts = Blog.objects.filter(status='Published', category=pk)
    # return HttpResponse(posts) working checked - status check in admin category
    
    # 1 - try-except block for error page
    # try:
    #     # fetch category name to be printed on category page- dynamic
    #     category = Category.objects.get(pk=pk)
    # except:  # noqa: E722 - 
    #     # try block failed - category doesn't exists - redirect then to homepage
    #       404 page to render if debug settings changed for deployment/production server. not in development server
    #     return redirect('home')
    
    # 2 - get object or 404 page - builtin django - 404 error page
    # fetch category name to be printed on category page- dynamic - OR USE CUSTOM 404 ERROR PAGE
    category = get_object_or_404(Category,pk=pk)
    
    context = {
        'posts':posts,
        'pk':pk,
        'category':category,
    }
    
    return render(request,'posts_by_category.html',context)


def blogs(request,slug):
    #fetch post exactly
    single_blog = get_object_or_404(Blog,slug=slug,status="Published")
    context = {
        'single_blog':single_blog
    }

    return render(request,'blogs.html',context)
