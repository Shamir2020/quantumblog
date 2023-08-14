from django.shortcuts import render, redirect
from pages.models import * 
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
def Home(request):
    blogs = Blog.objects.filter(featured=True)
    mainBlog = blogs[0]  
    return render(request,'home.html',{'blogs':blogs,'mainBlog':mainBlog})

def Blog_inside(request,id):
    commentForm = CommentForm()
    blog = Blog.objects.get(id=int(id))
    return render(request,'blog_inside.html',{'blog':blog,'commentForm':commentForm})

def createBlog(request):
    if request.user.is_authenticated:
        form = CreateBlogForm()
        if request.method == 'POST':
        
            form = CreateBlogForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request,'create_blog.html',{'form':form})
    else:
        return render(request,'notAuthorized.html',{})
    
def updateBlog(request,id):
    if request.user.is_authenticated:
        blog = Blog.objects.get(id=int(id))
        form = CreateBlogForm(instance=blog)
        
        if request.method == 'POST':
            form = CreateBlogForm(request.POST,request.FILES,instance=blog)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request,'update_blog.html',{'form':form})
    else:
        return render(request,'notAuthorized.html',{})
def DeleteBlog(request,id):
    blog = Blog.objects.get(id=int(id))
    blog.delete()
    return redirect('/')


def Blogs(request):
    
    blogs = Blog.objects.all().order_by('-created_at')
    page = request.GET.get('page')
    pages = Paginator(blogs,6)
    try:
        paginatedBlogs = pages.page(page)
    except:
        paginatedBlogs = pages.page(1)
    
    return render(request,'blogs.html',{'blogs':paginatedBlogs})

@login_required(login_url='signIn')
def addCommentToBlog(request):
    if request.method == 'POST':
        pass



def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if '@' in username:
            email = username 
            username = User.objects.get(email=email).username
            user = authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.error(request,'Invalid credentials!')

        else:
            user = authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.error(request,'Invalid credentials!')


    return render(request,'signIn.html',{})

def Register(request):
    
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists!')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email already exists!')
        elif password1 != password2:
            messages.error(request,'Passwords do not match!')
        else:
            user = User.objects.create_user(first_name=name,username=username,email=email,password=password1)
            user.save()
            profile = Profile.objects.create(user=user,name=name,email=email,)
            profile.save()
            auth.login(request, user)
            return redirect('/')


    return render(request,'signUp.html',{})

def Logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='signIn')
def UserDashboard(request, page):
    if page == 'dashboard':
        return  render(request,'user_dashboardInside.html',{})
    elif page == 'blogs':
        blogs = Blog.objects.filter(creator=request.user)
        page = request.GET.get('page')
        pages = Paginator(blogs,3)
        try:
            blogs = pages.page(page)
        except:
            blogs = pages.page(1)

        return render(request,'user_blogs.html',{'blogs':blogs})
    elif page == 'profile':
        return render(request,'user_profile.html',{})
    elif page == 'stories':
        return render(request,'user_stories.html',{})
    elif page == 'guides':
        return render(request,'user_guides.html',{})
    else:
        return  render(request,'user_dashboard.html',{})

@login_required(login_url='signIn')
def UploadProfilePhoto(request):
    
    profile, created = Profile.objects.get_or_create(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form2 = ProfileForm(request.POST,request.FILES,instance=profile)
        if form2.is_valid():
            form2.save()
            return redirect('/')

    return render(request,'upload_profile_photo.html',{'form':form})


