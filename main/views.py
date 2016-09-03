from django.shortcuts import render, get_object_or_404
from users.forms import loginForm, signupForm, editForm, changePassword
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import Film
from django import forms
from users.models import MyUser, Post, Comment, Notification
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json, random, datetime
from django.template import Context, Template
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

# YEARS = ['Year'] + list(range(2015, 1940, -1))
# MONTHS = ('Month', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
# DAYS = ['Day'] + list(range(1, 32))

def login_user(request):
    if request.method == "POST":
        form = loginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('timeLine'))

            else:
                form.add_error(None, 'Entered username or password is wrong')
                return render(request, 'signin.html', {'form': form})

        else:
            return render(request, 'signin.html', {'form': form})

    else:
        form = loginForm()
        return render(request, 'signin.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            newUser = MyUser()

            try:
                _newUser = User.objects.create_user(username=request.POST['username'], password=request.POST['password']
                                                    , first_name=request.POST['name'], email=request.POST['email'])
                newUser.user = _newUser
                newUser.birthday = request.POST['birthday_year'] + '-' + request.POST['birthday_month'] + '-' + \
                                   request.POST['birthday_day']
                newUser.save()

            except:
                form.add_error(None, 'username "' + request.POST['username'] + '" already existed')
                return render(request, 'signup.html', {'signupForm': form})

            return render(request, 'signin.html', {'form': loginForm(), 'msg': 'You have successfully registered,'
                                                                               ' login now'})

        else:
            return render(request, 'signup.html', {'signupForm': form})

    else:
        form = signupForm()
        return render(request, 'signup.html', {'signupForm': form})


def forget(request):
    return render(request, 'forget.html', {})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required()
def timeLine(request):
    followingUsers = MyUser.objects.get(user=request.user).followingUsers.all()
    posts = Post.objects.filter(user=followingUsers).order_by('-pubDate')[:1]

    return render(request, 'timeline.html', {'currUser': MyUser.objects.get(user=request.user), 'posts': posts})


@login_required()
def movie_profile(request, filmName):
    return render(request, 'movieProfile.html', {'film': get_object_or_404(Film, name=filmName),
                                                 'currUser': get_object_or_404(MyUser, user=request.user)})


@login_required()
def show_post(request, userID, postID):
    return render(request, 'post.html', {'user': get_object_or_404(MyUser, id=userID),
                                         'currUser': get_object_or_404(MyUser, user=request.user),
                                         'posts': Post.objects.filter(id=postID)})

@login_required()
def show_profile(request, userID):
    _user = get_object_or_404(MyUser, id=userID)
    requestUser = get_object_or_404(MyUser, user=request.user)

    return render(request, 'userProfile.html', {'user': _user,
                                                'currUser': requestUser,
                                                'posts': Post.objects.filter(user=_user)})

@csrf_exempt
@login_required()
def ajax_get_post(request, postNumber):
    if request.is_ajax():
        followingUsers = MyUser.objects.get(user=request.user).followingUsers.all()
        post = Post.objects.filter(user=followingUsers).order_by('-pubDate')[int(postNumber)]

        return HttpResponse(render(request, 'post_AJAX.html', {'user': post.user,
                                                               'currUser': get_object_or_404(MyUser, user=request.user),
                                                               'post': post}))


@csrf_exempt
@login_required()
def ajax_comment_on_post(request, postID):
    post = get_object_or_404(Post, id=postID)

    if request.is_ajax():
        tmpUsers = set()

        for cm in post.comment_set.all():
            tmpUsers.add(cm.user)

        for user in tmpUsers:
            if user != get_object_or_404(Post, id=postID).user and user.user != request.user:
                addNotification(request, user, postID, 4, True)

        comment = Comment()
        comment.user = get_object_or_404(MyUser, user=request.user)
        comment.post = post
        comment.body = json.loads(request.read().decode('utf-8'))['comment']
        comment.save()

        if request.user != get_object_or_404(Post, id=postID).user.user:
            addNotification(request, get_object_or_404(Post, id=postID).user, postID, 2, True)

        return render(request, 'comment_AJAX.html', {'cm': comment})

@csrf_exempt
@login_required()
def ajax_like_post(request, postID):
    if request.is_ajax():
        post = get_object_or_404(Post, id=postID)
        currUser = get_object_or_404(MyUser, user=request.user)

        if post.likeUsers.filter(user=currUser.user).count() == 0:
            if currUser != post.user:
                addNotification(request, get_object_or_404(Post, id=postID).user, postID, 1, True)
            post.likeUsers.add(currUser)
            return HttpResponse('Post successfully Liked !')

        else:
            addNotification(request, get_object_or_404(Post, id=postID).user, postID, 1, False)
            post.likeUsers.remove(currUser)
            return HttpResponse('unliked !')


@login_required()
def show_users(request, follow, userID):
    if follow == 'following':
        return render(request, 'person.html', {'users': get_object_or_404(MyUser, id=userID).followingUsers.all(),
                                               'currUser': get_object_or_404(MyUser, user=request.user)})

    elif follow == 'follower':
        return render(request, 'person.html', {'users': get_object_or_404(MyUser, id=userID).followerUsers.all(),
                                               'currUser': get_object_or_404(MyUser, user=request.user)})

@csrf_exempt
@login_required()
def follow_action(request, userID):
    if request.is_ajax():
        currUser = get_object_or_404(MyUser, user=request.user)
        tmpUser = get_object_or_404(MyUser, id=userID)

        if tmpUser not in currUser.followingUsers.all():
            addNotification(request, tmpUser, None, 3, True)
            currUser.followingUsers.add(tmpUser)
            tmpUser.followerUsers.add(currUser)

            return HttpResponse('successfully follow user')

        else:
            addNotification(request, tmpUser, None, 3, False)
            currUser.followingUsers.remove(tmpUser)
            tmpUser.followerUsers.remove(currUser)

            return HttpResponse('successfully unfollow user')


def addNotification(request, secondUser, postID, notificationState, isAdd):
    post = None

    try:
        post = get_object_or_404(Post, id=postID)
    except:
        pass

    currUser = get_object_or_404(MyUser, user=request.user)
    tmpUser = secondUser

    notification = Notification()
    notification.firstUser = currUser
    notification.secondUser = tmpUser
    notification.post = post
    notification.notificationState = notificationState
    notification.save()

    if isAdd:
        currUser.first.add(notification)
        tmpUser.second.add(notification)

    else:
        Notification.objects.filter(firstUser=notification.firstUser).filter(secondUser=notification.secondUser) \
                                        .filter(post=notification.post) \
                                        .filter(notificationState=notification.notificationState).delete()


def search(request):
    searchText = request.GET['search']
    type = int(request.GET['type'])
    isInSearchPage = True if request.GET.get('isInSearch', False) is not False else False

    if request.is_ajax():
        if searchText != '':
            if type == 1:
                films = Film.objects.filter(name__contains=searchText)[:5]
                return render(request, 'search_result_film.html', {'films': films, 'isInSearch': isInSearchPage})

            if type == 2:
                users = MyUser.objects.filter(user__username__contains=searchText)[:5]
                return render(request, 'search_result_users.html', {'users': users, 'isInSearch': isInSearchPage,
                                                                    'currUser': get_object_or_404(MyUser, user=request.user)})

    else:
        if searchText != '':
            films = Film.objects.filter(name__contains=searchText)
            users = MyUser.objects.filter(user__username__contains=searchText)
            return render(request, 'search.html', {'films': films, 'users': users,
                                                   'currUser': get_object_or_404(MyUser, user=request.user)})
        else:
            return render(request, 'search.html', {'currUser': get_object_or_404(MyUser, user=request.user)})

@login_required()
@csrf_exempt
def create_post(request, filmID):
    film = get_object_or_404(Film, id=filmID)
    currUser = get_object_or_404(MyUser, user=request.user)
    body = request.POST['postBody']
    rate = int(request.POST['rate'])

    if request.POST['postBody'] != '':
        newPost = Post()
        newPost.body = body
        newPost.film = film
        newPost.score = rate
        newPost.user = currUser
        newPost.save()

        numberOfPosts = Post.objects.filter(film=film).count()
        average = (((film.averageScore * (numberOfPosts-1)) + rate)/numberOfPosts)
        Film.objects.filter(id=filmID).update(averageScore=average)

        return HttpResponseRedirect(reverse('showPost', args=[currUser.id, newPost.id]))

@login_required()
@csrf_exempt
def random_aside(request):
    films = Film.objects.all()
    random_numbers = random.sample(range(films.count()), min(3, films.count()))
    random_list = []

    for i in random_numbers:
        tmp = {'type': 'film', 'name': films[i].name, 'picture': films[i].picture.url,
               'rate': films[i].averageScore, 'profile': reverse('movieProfile', args=[films[i].name])}
        random_list.append(tmp)


    currUser = get_object_or_404(MyUser, user=request.user)
    users = MyUser.objects.exclude(Q(id__in=currUser.followingUsers.all()) | Q(id=currUser.id))
    random_user = currUser

    if users.count() > 0:
        random_user = users[random.randint(0, users.count()-1)]
    
    random_list.append({'type': 'user', 'name': random_user.user.username, 'picture': random_user.profilePicture.url,
                        'profile': reverse('showProfile', args=[random_user.id]),
                        'age': datetime.datetime.now().year - random_user.birthday.year})

    return HttpResponse(json.dumps(random_list))


@login_required()
def edit_profile(request):
    user = get_object_or_404(MyUser, user=request.user)

    if request.method == 'GET':
        return render(request, 'edit_profile.html', {'currUser': user,
                                                     'user': user,
                                                     'form': editForm(user=user)})

    else:
        form = editForm(request.POST, request.FILES, user=user, instance=user)

        if form.is_valid():
            form.save()
            User.objects.filter(id=user.user.id).update(first_name=form.cleaned_data['name'])
            return render(request, 'userProfile.html', {'currUser': user,
                                                        'user': user,
                                                        'posts': Post.objects.filter(user=user)})

        else:
            return render(request, 'edit_profile.html', {'currUser': user,
                                                         'user': user,
                                                         'form': form})


@login_required()
def change_password(request):
    user = get_object_or_404(MyUser, user=request.user)

    if request.method == "GET":
        return render(request, 'change_password.html', {'currUser': user, 'user': user, 'form': changePassword()})

    else:
        form = changePassword(request.POST)

        if form.is_valid():
            if user.user.check_password(request.POST['current_Password']):
                request.user.set_password(request.POST['new_Password'])
                request.user.save()

                newUser = authenticate(username=request.user.username, password=request.POST['new_Password'])
                login(request, newUser)

                return render(request, 'userProfile.html', {'currUser': user, 'user': user, 'form': form,
                                                            'posts': Post.objects.filter(user=user)})

            else:
                form.add_error(None, 'Entered password is wrong')
                return render(request, 'change_password.html', {'currUser': user, 'user': user, 'form': form})

        else:
            return render(request, 'change_password.html', {'currUser': user, 'user': user, 'form': form})
