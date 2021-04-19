from django.urls import path
from . import views

urlpatterns = [
    #path('',include('sislaf.urls'))
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('search',views.search, name='search'),
    path('search_a/<str:movie_name>',views.search_a, name='search_a'),
    path('actor_details/<str:actor_name>',views.actor_details, name='actor_details'),
]