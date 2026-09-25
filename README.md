# 🎬 Movie Website

A movie website developed using **Python and Django**. The application allows users to browse movies, view movie details, search for movies, add comments, manage favourites, and manage their own movie entries.

## 🚀 Features

- User registration
- User login and logout
- Browse movies
- Search movies
- Browse movies by category
- View movie details
- Add movies
- Edit movies
- Delete movies
- Upload movie images
- Add comments to movies
- Add and remove movies from favourites
- View favourite movies
- User profile
- Edit user profile
- Django admin panel

## 🛠️ Technologies Used

- **Python**
- **Django**
- **HTML**
- **CSS**
- **JavaScript**
- **SQLite**

## 📁 Project Structure

```text
movie_website/
│
├── manage.py
├── README.md
│
├── media/
│   └── movies/
│       ├── inception_2010.jpg
│       ├── infinity_war_2018.jpg
│       ├── interstellar_2014.jpg
│       └── ...
│
├── movie_app/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_comment.py
│   │   ├── 0003_favourite.py
│   │   ├── 0004_remove_movies_release_date_movies_release_year.py
│   │   └── __init__.py
│   │
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── add_movie.html
│   │   ├── base.html
│   │   ├── delete_movie.html
│   │   ├── edit_movie.html
│   │   ├── edit_profile.html
│   │   ├── favourites.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── movie_detail.html
│   │   ├── profile.html
│   │   └── register.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
└── movie_website/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
