from django.shortcuts import get_object_or_404, render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from assignments.models import About
from blog_main.forms import RegistrationForm
from .models import  Category,Blog,Comment
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.core.mail import send_mail
from django.conf import settings

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
        # 'posts2':posts2,
    }
    
    return render(request,'posts_by_category.html',context)


def blogs(request,slug):
    
    single_blog = get_object_or_404(Blog,slug=slug,status="Published")
    
    
    #add comment
    if request.method=='POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
        
        
    # Comments
    comments = Comment.objects.filter(blog = single_blog)
    # print("Comment -> ", comments)
    comment_count = comments.count()
    
    context = {
        'single_blog':single_blog,
        'comments':comments,
        'comment_count':comment_count,
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    # print('keywrod=> ',keyword)
    
    #title = for title search keyword - ut for body search keyword description/body-  OR operator Q objects -- comma(,)-and operator
    blogs = Blog.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains = keyword) | Q(blog_body__icontains = keyword) , status = "Published")
    print(blogs)
    
    context = {
        'blogs':blogs,
        'keyword':keyword,
    }
    
    return render(request,'search.html',context)

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()
            send_mail("Welcome to Django Blogs","Congratulations on creating account!!",settings.DEFAULT_FROM_EMAIL,[current_user.email])
            return redirect('login')
        
    else:
        form = RegistrationForm()
        
    context = {
        'form':form,
    }
    return render(request,'register.html',context)

def login(request):
    
    if request.method=='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    context = {
        'form':form,
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')

