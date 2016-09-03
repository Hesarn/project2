from django.db import models
from django.contrib.auth.models import User
import datetime
from Project2.settings import STATIC_URL

class MyUser(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()
    followingUsers = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='following')
    followerUsers = models.ManyToManyField('self', blank=True, symmetrical=False)
    profilePicture = models.ImageField(upload_to='photo/', default='user.png')

    def __str__(self):
        return self.user.username

    def natural_key(self):
        return self.id, self.user.username, self.profilePicture.url


class Film(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='photo/', default='user.png')
    description = models.TextField()
    averageScore = models.FloatField(default=0)
    imdbLink = models.CharField(max_length=200)
    profileLink = models.CharField(max_length=200, default='movieProfile.html')

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name, self.picture.url


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cast(models.Model):
    person = models.ForeignKey(Person, null=True)
    roleName = models.CharField(max_length=100)
    film = models.ForeignKey(Film)

    def __str__(self):
        return self.person.name


class Post(models.Model):
    user = models.ForeignKey(MyUser)
    film = models.ForeignKey(Film)
    score = models.IntegerField()
    body = models.TextField()
    pubDate = models.DateTimeField(default=datetime.datetime.now)
    likeUsers = models.ManyToManyField(MyUser, related_name='like', blank=True)

    def __str__(self):
        return self.user.user.username + ' posted about ' + self.film.name


class Comment(models.Model):
    user = models.ForeignKey(MyUser)
    post = models.ForeignKey(Post)
    body = models.TextField()

    def __str__(self):
        return self.user.user.username + ' commented on ' + self.post.user.user.username + "'s post"


class Notification(models.Model):
    firstUser = models.ForeignKey(MyUser, related_name='first')
    secondUser = models.ForeignKey(MyUser, related_name='second')
    post = models.ForeignKey(Post, blank=True, null=True)
    notificationState = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.firstUser.user.username + ' to ' + self.secondUser.user.username
