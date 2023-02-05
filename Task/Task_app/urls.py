
from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static 

urlpatterns = [
   
    path('',views.home,name='home'),
    path('login_p',views.login_p,name='login_p'),
    path('signup',views.signup,name='signup'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('login_page',views.login_page,name='login_page'),
    path('show_students',views.show_students,name='show_students'),
    path('usercreate/',views.usercreate,name="usercreate"),
    path('about',views.about,name='about'),
    path('profile',views.profile,name='profile'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('delete_student/<int:pk>',views.delete_student,name='delete_student'),
    path('show_student/<int:pk>',views.show_student,name='show_student'),
    path('logout',views.logout,name='logout'),
    #path('profile_page',views.profile_page,name='profile_page'),
    path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 