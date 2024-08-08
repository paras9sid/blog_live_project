from django.shortcuts import get_object_or_404, render,redirect,HttpResponseRedirect
from .models import  Category,Blog,Comment
from django.db.models import Q




def posts_by_category(request,pk):
    # print(pk) # working checked 
    # return HttpResponse('<h2>Posts by category!!</h2>') # working checked
    

    # fetch the post belong to id/pk of category
    posts = Blog.objects.filter(status='Published', category=pk).order_by('-updated_at')
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
    
    single_blog = get_object_or_404(Blog, slug=slug, status="Published")
    print(single_blog)
        
    # # #add comment
    # if request.method=='POST':
    #     comment = Comment()
    #     comment.user = request.user
    #     comment.blog = single_blog
    #     comment.comment = request.POST['comment']
    #     comment.save()
    #     return HttpResponseRedirect(request.path_info)
            
    # # Comments
    # comments = Comment.objects.filter(blog = single_blog)
    # # print("Comment -> ", comments)
    # comment_count = comments.count()
    
    context = {
        'single_blog':single_blog,
    #     'comments':comments,
    #     'comment_count':comment_count,
    }
    return render(request,'blogs.html',context)

def search(request):
    
    keyword = request.GET.get('keyword')
    if keyword:
        print('keyword=> ',keyword)
    else:
        print('not valid')
    
    #title = for title search keyword - ut for body search keyword description/body-  OR operator Q objects -- comma(,)-and operator
    blogs = Blog.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains = keyword) | Q(blog_body__icontains = keyword) , status = "Published")
    print(blogs)
    
    context = {
        'blogs':blogs,
        'keyword':keyword,
    }
    
    return render(request,'search.html',context)






