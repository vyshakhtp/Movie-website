from django.urls import path
from . import views

urlpatterns=[
    path("register/",views.register_view,name="register"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("",views.home_view,name="home"),
    path("add_movie/",views.add_movie,name="add_movie"),
    path("category/<int:category_id>/",views.category_movies,name="category_movies"),
    path("movie/<int:movie_id>/",views.movie_detail,name="movie_detail"),
    path("edit_movie/<int:movie_id>/",views.edit_movie,name="edit_movie"),
    path("delete_movie/<int:movie_id>/",views.delete_movie,name="delete_movie"),
    path("movie/<int:movie_id>/comment/",views.add_comment,name="add_comment"),
    path("movie/<int:movie_id>/favorite",views.favourite_view,name="favourite_view"),
    path("favorites/",views.favourite_movies,name="favourite_movies"),
    path("profile/",views.profile_view,name="profile_view"),
    path("profile/edit/",views.edit_profile,name="edit_profile"),
]
