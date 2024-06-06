from django.urls import path
from . import views

urlpatterns = [
    # <int:pk>/ or <int:category_id>/ -> same should be written in parenthesis in views - 
    path('<int:pk>/',views.posts_by_category,name='posts_by_category'),
]

