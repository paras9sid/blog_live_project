from django.urls import path
from . import views


urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    
    # Category CRUD
    
    # read
    path('categories/',views.categories,name='categories'),
    
    # crud - create/add
    path('categories/addcategoriesNew/',views.add_category,name='add_category'),
    
    # crud - update/edit
    path('categories/editcategoriesOld/<int:pk>',views.edit_category,name='edit_category'),
    
    # crud - delete
    path('categories/deletecategoriesNewOld/<int:pk>',views.delete_category,name='delete_category'),
        
    
    # Posts - CRUD
    
    # read
    path('posts/',views.posts,name='posts'),
    
    # create
    path('posts/addpostsNew/',views.add_post,name='add_post'),
    
    # edit/update
    path('posts/editpostsOld/<int:pk>/',views.edit_post,name='edit_post'),
    
    # delete
    path('posts/deletepostsNewOld/<int:pk>/',views.delete_post,name='delete_post'),
    
    
    # users
    path('users/',views.users,name='users'),

    # add user - Create
    path('users/addusersNew/',views.add_user,name='add_user'),
    
    # Update/edit
    path('users/editusersOld/<int:pk>/',views.edit_user,name='edit_user'),
    
    # delete
    path('users/deleteusersNewOld/<int:pk>/',views.delete_user,name='delete_user'),

    
]
