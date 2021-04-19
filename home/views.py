from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from pprint import pprint

#------------- import models -------------------
from .models import Movies
from .models import Artist
from .models import Movies_artists
# Create your views here.
def  index(request):
    movies = Movies.objects.all().order_by('-year_of_release')
    artist = Artist.objects.all()[:4]
    artist_1 = Artist.objects.all()[4:8]
    current_year_movies = Movies.objects.filter(year_of_release=2017).order_by('-year_of_release')
    # movies = Movies.objects.get(id=1)
    return render(request,'index.html',{'m':movies,'a':artist,'cm':current_year_movies,'a1':artist_1})

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save()
        print('user created')
        # return redirect('/')
    #     if password1 == password2:
    #         if User.objects.filter(username=username).exists:
    #             messages.info(request,'Username Taken')
    #             print('Username taken')
    #             return redirect('register')
    #         elif User.objects.filter(email=email).exists:
    #             messages.info(request,'Email Taken')
    #             print('email taken')
    #             return redirect('index')
    #         else:
    #             user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
    #             user.save()
    #             print('user created')
    #             return redirect('/')
    #     else:
    #         print('Password not Matching....')
    #         messages.info(request,'Password not matches')
    #         return redirect('register')
    #     return redirect('/')
    # else:
        return render(request,'index.html')

def  login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Invalid Credentials..')
            return redirect('index')
    else:
        return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def search(request):
    if request.method == 'POST':
        # ax = request.GET['username']
        ax = request.POST['search_items']
        sc = request.POST['search_category']
        if sc == 'movie' and ax is not None:
            search_ = Movies.objects.filter(movie_name=ax)
            if not search_:
                return render(request,'test.html',{'b': 'Data not found!','search_':search_})
            else: 
            # # print(search_)
                search_result = Movies.objects.get(movie_name=ax)
                # search_.id
                movie_id_result = search_result.movie_id

                # search_actor_result = Movies_artists.objects.get(movie_id=movie_id_result)
                search_actor_result = Movies_artists.objects.filter(movie_id_id=int(movie_id_result))
                if not search_actor_result:
                    return render(request,'test.html',{'a': ax, 's':search_result,'search_': search_}) 
                else:
                    
                    for bb in search_actor_result:
                        print(bb.artist_id_id,bb.artist_id.artist_name)
                    pprint(search_actor_result[1].artist_id_id)
                    print(search_actor_result.count())
                    print(request.POST['search_items'])
                    return render(request,'test.html',{'a': ax, 's':search_result,'search_': search_,'actor_result':search_actor_result,'actor_count': search_actor_result.count()})
        elif sc == 'actor':
            search_ = Artist.objects.filter(artist_name=ax)
            if not search_:
                return render(request,'celebrity_single.html',{'b': 'Data not found!','search_':search_})
            else: 
            # # print(search_)
                search_result = Artist.objects.get(artist_name=ax)
                # search_.id
                actor_id_result = search_result.artist_id
                search_movie_result = Movies_artists.objects.filter(artist_id_id=int(actor_id_result))
                if not search_movie_result:
                    return render(request,'celebrity_single.html',{'a': ax, 's':search_result,'search_': search_}) 
                else:
                    for bb in search_movie_result:
                        print(bb.movie_id_id,bb.movie_id.movie_name)
                    print(search_movie_result.count())
                    print(request.POST['search_items'])
                    return render(request,'celebrity_single.html',{'a': ax, 's':search_result,'search_': search_,'movie_count':search_movie_result.count(), 'movie_result': search_movie_result})
            # return redirect('/')

def search_a(request, movie_name):
    search_ = Movies.objects.filter(movie_name=movie_name)
    search_result = Movies.objects.get(movie_name=movie_name)
                # search_.id
    movie_id_result = search_result.movie_id

    # search_actor_result = Movies_artists.objects.get(movie_id=movie_id_result)
    search_actor_result = Movies_artists.objects.filter(movie_id_id=int(movie_id_result))
    if not search_actor_result:
        return render(request,'test.html',{ 's':search_result,'search_': search_}) 
    else:
        
        for bb in search_actor_result:
            print(bb.artist_id_id,bb.artist_id.artist_name)
        
        return render(request,'test.html',{ 's':search_result,'search_': search_,'actor_result':search_actor_result,'actor_count': search_actor_result.count()})
    # context = {'movie_name': movie_name}

    # return render(request,'test.html', {'s':search_result})

def actor_details(request, actor_name):
    search_ = Artist.objects.filter(artist_name=actor_name)
    search_result = Artist.objects.get(artist_name=actor_name)
                # search_.id
    actor_id_result = search_result.artist_id
    search_movie_result = Movies_artists.objects.filter(artist_id_id=int(actor_id_result))
    if not search_movie_result:
        return render(request,'celebrity_single.html',{'s':search_result,'search_': search_}) 
    else:
        return render(request,'celebrity_single.html',{ 's':search_result,'search_': search_,'movie_count':search_movie_result.count(), 'movie_result': search_movie_result})
