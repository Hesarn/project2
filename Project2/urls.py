from django.conf.urls import include, url
from django.contrib import admin
#from .settings import MEDIA_ROOT
import django
from main import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Project2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': MEDIA_ROOT, }),

    url(r'^captcha/', include('captcha.urls')),

    url(r'^login/$', views.login_user, name="login"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^forget/$', views.forget, name="forget"),
    url(r'^timeline/$', views.timeLine, name="timeLine"),
    url(r'^logout/$', views.logout_user, name="logout"),
    url(r'^movieProfile/(\w+)$', views.movie_profile, name="movieProfile"),
    url(r'^post/(\d+)/(\d+)$', views.show_post, name='showPost'),
    url(r'^profile/(\d+)$', views.show_profile, name='showProfile'),
    url(r'^ajax/(\d+)$', views.ajax_get_post),
    url(r'^ajax/commentOnPost/(\d+)$', views.ajax_comment_on_post, name='comment'),
    url(r'^ajax/likePost/(\d+)$', views.ajax_like_post, name='likePost'),
    url(r'^users/(\w+)/(\d+)$', views.show_users, name='showUsers'),
    url(r'^ajax/follow_unfollow/(\d+)$', views.follow_action, name='followUnfollow'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search/(\w+)$', views.search),
    url(r'^createPost/(\d+)$', views.create_post, name='createPost'),
    url(r'^ajax/aside$', views.random_aside, name='aside'),
    url(r'^edit$', views.edit_profile, name='editProfile'),
    url(r'^change-password$', views.change_password, name='changePassword'),
]
