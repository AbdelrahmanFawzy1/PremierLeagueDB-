
from django.db import router
from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import  LogIn, Register, \
                    list_Reviews, post,\
                    PlayersByName,PlayersByPosition,PlayersByNationality,\
                    ClubByName,ClubByCity,ClubByStadium,\
                    MostWonBySeason,TotalWins,TotalHomeWins,TotalYellowCards,TotalFouls,Totalshots
                    


urlpatterns=[

    path('User/LogIn', LogIn),
    path('User/Register', Register),

    path('Reviews/get', list_Reviews),
    path('Reviews/set', post),



    path('Player/byname', PlayersByName),
    path('Player/byposition', PlayersByPosition),
    path('Player/bycountry', PlayersByNationality),

    path('Club/byname', ClubByName),
    path('Club/bycity', ClubByCity),
    path('Club/bystadium', ClubByStadium),


    path('TopTeams/mostwinseason', MostWonBySeason),
    path('TopTeams/mostwin', TotalWins),
    path('TopTeams/mosthomewin', TotalHomeWins),
    path('TopTeams/mostyellow', TotalYellowCards),
    path('TopTeams/mostfouls', TotalFouls),
    path('TopTeams/mostshots', Totalshots),

]