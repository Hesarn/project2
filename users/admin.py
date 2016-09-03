from django.contrib import admin
from .models import MyUser, Post, Cast, Comment, Film, Notification, Person

admin.site.register(MyUser)
admin.site.register(Post)
admin.site.register(Cast)
admin.site.register(Comment)
admin.site.register(Film)
admin.site.register(Notification)
admin.site.register(Person)
