from django.urls import path
from . import views
urlpatterns = [
    path('getFeaturedBlogs',views.getFeaturedBlogs,name='getFeaturedBlogs'),
    path('getAllBlogs',views.getAllBlogs,name='getAllBlogs'),
]