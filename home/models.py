from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_id = models.IntegerField(primary_key=True, serialize= False)
    # 'artist_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    movie_name = models.CharField(max_length=200)
    year_of_release = models.IntegerField()
    genre = models.CharField(max_length=100)
    trailer_link = models.CharField(max_length=1000,null=True, blank=True)
    poster_link = models.CharField(max_length=200,null=True, blank=True)
    language = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=2000,null=True, blank=True)
    run_time = models.IntegerField()
    director = models.CharField(max_length=300)

class Artist(models.Model):
    artist_id = models.IntegerField(primary_key=True,serialize=False)
    artist_name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=500,null=True, blank=True)
    gender = models.CharField(max_length=45)
    brief_info = models.CharField(max_length=2000,null=True, blank=True)

class Movies_artists(models.Model):
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE,blank=True,null=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE,blank=True,null=True)
 
    class Meta:
        unique_together = (('movie_id', 'artist_id'),)