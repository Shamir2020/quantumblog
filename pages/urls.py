from django.urls import path 
from . import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('blog/<str:id>',views.Blog_inside,name='blogInside'),
    path('createBlog',views.createBlog,name='createBlog'),
    path('updateBlog/<str:id>',views.updateBlog,name='updateBlog'),
    path('deleteBlog/<str:id>',views.DeleteBlog,name='deleteBlog'),
    path('blogs',views.Blogs,name='blogs'),
    path('signin',views.Login,name='signIn'),
    path('signup',views.Register,name='signUp'),
    path('logout',views.Logout,name='logout'),
    path('userdashboard/<str:page>',views.UserDashboard,name='userDashboard'),
    path('uploadprofilephoto',views.UploadProfilePhoto,name='uploadProfilePhoto'),
    path('addCommentToBlog',views.addCommentToBlog,name='addCommentToBlog'),
]