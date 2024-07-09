from django.urls import path
from . import views


urlpatterns = [
    path('/',views.dashboard,name='dashboard'),
    path('/categories/',views.categories,name='categories'),
    
    # crud - create/add
    path('/categories/add/',views.add_category,name='add_category'),
    
    # crud - update/edit
    path('/categories/edit/<int:pk>',views.edit_category,name='edit_category'),
    
    # crud - delete
    path('/categories/delete/<int:pk>',views.delete_category,name='delete_category'),

    
]
