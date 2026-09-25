from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movies(models.Model):
    title=models.CharField(max_length=100)
    poster=models.ImageField(upload_to="movies/")
    description=models.TextField(null=True)
    release_year=models.IntegerField()
    actors=models.CharField(max_length=500)
    ratings=models.DecimalField(max_digits=3,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name="movies")
    trailer=models.URLField()
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE,related_name="comments")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"

class Favourite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Mete:
        constraints=models.UniqueConstraint(fields=["user","movie"],name="unique_user_movie_favourite")
    def __str__(self):
        return f"{self.user.username}-{self.movie.title}"
