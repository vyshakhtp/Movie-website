from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm,MovieForm,CommentForm,ProfileForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Movies,Category,Favourite
from django.db.models import Q
from django.contrib import messages


def register_view(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,f"welcome {user.username}!Youre account has been created successfully ")
            return redirect("login")

    else:
        form=RegisterForm()
    return render(request,"register.html",{"form":form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("home")

    else:
        form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            movie=form.save(commit = False)
            movie.created_by = request.user
            movie.save()
            return redirect("home")
    else:
        form = MovieForm()
    return render(request,"add_movie.html",{"form":form})

def home_view(request):
    search=request.GET.get('q',"")
    categories = Category.objects.all()
    if search:
        movies=Movies.objects.filter(Q(title__icontains=search)|Q(category__name__icontains= search))
    else:
        movies=Movies.objects.all()
    
    return render(request,"home.html",{"movies":movies,"categories":categories,"search":search})

def category_movies(request,category_id):
    category = get_object_or_404(Category, id=category_id)
    movies=category.movies.all()
    categories = Category.objects.all()
    return render(request,"home.html",{"movies":movies,"categories":categories,"search":""})



@login_required
def edit_movie(request,movie_id):
    movie=get_object_or_404(Movies,id=movie_id)
    if movie.created_by != request.user:
        return redirect("home")
    if request.method == 'POST':
        form=MovieForm(request.POST,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movie_detail",movie_id=movie.id)
    else:
        form=MovieForm(instance=movie)
    return render(request,"edit_movie.html",{"form":form,"movie":movie})

@login_required
def delete_movie(request,movie_id):
    movie=get_object_or_404(Movies,id=movie_id)
    if movie.created_by != request.user:
        return redirect("home")
    if request.method == 'POST':
        movie.delete()
        return redirect("home")
    return render(request,"delete_movie.html",{"movie":movie})

@login_required
def add_comment(request,movie_id):
    movie = get_object_or_404(Movies,id=movie_id)
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=request.user
            comment.movie=movie
            comment.save()
            return redirect("movie_detail",movie_id=movie.id)
    else:
        form=CommentForm()
        return render(request,"movie_detail.html",{"form":form,"movie":movie})

def movie_detail(request,movie_id):
    movie=get_object_or_404(Movies,id=movie_id)
    comments=movie.comments.all()
    form = CommentForm()
    is_favourite = False
    if request.user.is_authenticated:
        is_favourite = Favourite.objects.filter(user=request.user,movie=movie).exists()
    return render(request,"movie_detail.html",{"movie":movie,"comments":comments,"form":form,"is_favourite":is_favourite})

@login_required
def favourite_view(request,movie_id):
    movie = get_object_or_404(Movies,id=movie_id)
    favourite = Favourite.objects.filter(user=request.user,movie=movie).first()
    if favourite:
        favourite.delete()
    else:
        Favourite.objects.create(user=request.user,movie=movie)

    return redirect("movie_detail",movie_id=movie.id)

@login_required
def favourite_movies(request):
    favourites = Favourite.objects.filter(user=request.user).select_related("movie")
    return render(request,"favourites.html",{"favourites":favourites})

@login_required
def profile_view(request):
    return render(request,"profile.html",{"profile_user":request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile_view")
    else:
        form = ProfileForm(instance=request.user)
    return render(request,"edit_profile.html",{"form":form})