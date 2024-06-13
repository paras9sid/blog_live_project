from django.shortcuts import get_object_or_404, render,redirect
from blog_app.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, CategoryForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    
    context = {
        'category_count':category_count,
        'blogs_count':blogs_count,
    }
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

# CRUD - Create
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    context = {
        'form':form,
    }
    return render(request,'dashboard/add_category.html',context)

#CRUD - update
def edit_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method=='POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)

    context = {
        'form':form,
        'category':category,
    }
    return render(request,'dashboard/edit_category.html',context)

def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')


#POSTS CRUD

# read
def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts,
    }
    return render(request,'dashboard/posts.html',context)

#create
def add_post(request):
    
    if request.method == 'POST':
        
        #request.FILES - image field error handling
        form = BlogPostForm(request.POST,request.FILES)
        
        if form.is_valid():
            
            # author blank error handling
            post = form.save(commit=False) # temporarily saving the form
            #request.user - user logged in and creating posts
            post.author = request.user
            post.save()
            
            # unique blank slug error handling
            title = form.cleaned_data['title']
            # this is a new post-1 added again - 2 become -- working on pkey
            post.slug = slugify(title) + '-' + str(post.pk)
            post.save()
            
            return redirect('posts')
        else:
            print('form is invalid')
            print(form.errors)

    form = BlogPostForm()

    context = {
        'form':form,
    }
    return render(request,'dashboard/add_post.html',context)
    

# Update/Edit

def edit_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    if request.method=='POST':
        form = BlogPostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)+'-'+str(post.pk)
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context ={
        'form':form,
        'post':post,
    }        
    return render(request,'dashboard/edit_post.html',context)


# delete
def delete_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')


def users(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request,'dashboard/users.html',context)