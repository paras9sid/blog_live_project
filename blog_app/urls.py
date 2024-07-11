from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # <int:pk>/ or <int:category_id>/ -> same should be written in parenthesis in views - 
    path('<int:pk>/',views.posts_by_category,name='posts_by_category'),
    
    #password manage
    
    # 1- allow email to recv passwork link
    path('reset_password',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    
    # 2- show success message - sent email stating that password reset
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_sent.html'),name='password_reset_done'),
    
    # 3- send a link to email so taht we reset pur password
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_form.html'),name='password_reset_confirm'),
    
    # 4- success message password changed
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),name='password_reset_complete'),
]

