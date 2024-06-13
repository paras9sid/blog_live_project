from django.urls import path
from . import views


urlpatterns = [
    path('/',views.dashboard,name='dashboard'),
    
    # Category CRUD
    
    # read
    path('/categories/',views.categories,name='categories'),
    
    # crud - create/add
    path('categories/add/',views.add_category,name='add_category'),
    
    # crud - update/edit
    path('categories/edit/<int:pk>',views.edit_category,name='edit_category'),
    
    # crud - delete
    path('categories/delete/<int:pk>',views.delete_category,name='delete_category'),
        
    
    # Posts - CRUD
    
    # read
    path('/posts/',views.posts,name='posts'),
    
    # create
    path('posts/add/',views.add_post,name='add_post'),
    
    # edit/update
    path('posts/edit/<int:pk>',views.edit_post,name='edit_post'),
    
    # delete
    path('posts/delete/<int:pk>',views.delete_post,name='delete_post'),
    
    

    
]
