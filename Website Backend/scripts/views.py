from lib2to3.pgen2 import token
from os import stat
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import mysql.connector
from django.db import  DatabaseError, IntegrityError
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

import mysql.connector

cnx = mysql.connector.connect(
 host="sql4.freemysqlhosting.net",
 user="sql4490151",
 password="C79y227fa5",
 database="sql4490151",
 port= '3306',
)

cursor= cnx.cursor()

#User 

@api_view(['POST'])
def LogIn (request):
        data= JSONParser().parse(request)
        cursor.execute('SELECT UserEmail, UserName FROM FanUser WHERE \
                        UserEmail= %s AND Password= md5(%s);', (data['UserEmail'],data['Password']))    
        User= cursor.fetchall()
        print(User)
        UserCol=['UserEmail', 'UserName']
        if User:
            json_data = [dict(zip(UserCol, row)) for row in User]
            json_data.append({'status':'202'})
            return Response(json_data)
        else:
            json_data=[{},{'status': '403'}]
            return Response(json_data)

@api_view(['POST'])
def Register(request):
        
        data= JSONParser().parse(request)
        try:
            cursor.execute('INSERT INTO FanUser \
                            VALUES (%s,%s,%s,%s,%s,md5(%s));', (data['UserEmail'], data['UserName'],data['Gender'], data['DateOfBirth'] \
                            ,data['FavouriteClubName'],data['Password']))
            cnx.commit()

        except DatabaseError or IntegrityError:
            return Response(status= status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status= status.HTTP_201_CREATED)


def isValidMatch(match):

    cursor.execute('SELECT * FROM MatchGame \
            Where MatchDate=%s and Home_ClubName=%s and Away_ClubName=%s', \
            (match['MatchDate'], match['Home_ClubName'],match['Away_ClubName']))
        
    MatchList= cursor.fetchall()
        
    if not MatchList: 
        return False
    else:
        return True


@api_view(['POST'])
def list_Reviews(request):

    data= JSONParser().parse(request)
        
    if not isValidMatch(data):
        return Response([{'Message':"Match Not Exist"}])

    cursor.execute('SELECT * FROM FanUserMatchReview \
                    Where MatchDate=%s and Home_ClubName=%s and Away_ClubName=%s;', \
                    (data['MatchDate'], data['Home_ClubName'],data['Away_ClubName']))
        
    reviews= cursor.fetchall()

    if not reviews: return Response([{'Message':"Be The First One To Review This Match"}])

    Reviews_columns = ['UserEmail','MatchDate','Home_ClubName','Away_ClubName','Rate','TextReview']

    json_data = [dict(zip(Reviews_columns, row)) for row in reviews]

    return Response(json_data)


@api_view(['POST'])
def post(request):
        
    data= JSONParser().parse(request)
    cursor.execute('INSERT INTO FanUserMatchReview \
                    VALUES (%s , %s , %s , %s , %s , %s);', (data['UserEmail'], data['MatchDate'],data['Home_ClubName'], \
                    data['Away_ClubName'],data['Rate'],data['TextReview']))
    cnx.commit()

    #check if valid
    cursor.execute('Select * from FanUserMatchReview \
                   where UserEmail=%s;', (data['UserEmail'],))

    NewUser= cursor.fetchall()
    if NewUser:
        return Response()
    else:
        return Response()


Players_cols = ['PlayerName','DateOfBirth','Nationality','Weight','Height','PlayingPosition']

@api_view(['POST'])
def PlayersByNationality(request):
            
    data= JSONParser().parse(request)

    cursor.execute('SELECT Player_Name, P_ClubName, Season \
                            From Player P inner join PlayerForClub PC  \
                            On P.PlayerName= PC.Player_Name \
                            where P.Nationality= %s;', (data['Nationality'],))
            
    Players= cursor.fetchall()

    if not Players: return Response([{'Message':"No Players Exist"}])

    json_data = [dict(zip(['Player_Name', 'P_ClubName','Season'], row)) for row in Players]

    return Response(json_data)

@api_view(['POST'])
def PlayersByName(request):

    data= JSONParser().parse(request)

    cursor.execute('SELECT * \
                    From Player P   \
                    where P.PlayerName= %s;', (data['PlayerName'],))
            
    Players= cursor.fetchall()

    if not Players: return Response([{'Message':"No Player Exist"}])

    json_data = [dict(zip(Players_cols, row)) for row in Players]

    return Response(json_data)


@api_view(['POST'])
def PlayersByPosition(request):
            
    data= JSONParser().parse(request)

    cursor.execute('SELECT * \
                    From Player P   \
                    where P.PlayingPosition= %s;', (data['PlayingPosition'],))
            
    Players= cursor.fetchall()

    if not Players: return Response([{'Message':"No Player Exist"}])

    json_data = [dict(zip(Players_cols, row)) for row in Players]

    return Response(json_data)

##################################################################
##CLUB

CityCols=['ClubName', 'StadiumName', 'Website']

@api_view(['POST'])
def ClubByName(request):
            
    data= JSONParser().parse(request)

    cursor.execute('SELECT * \
                    From Club    \
                    where ClubName= %s;', (data['ClubName'],))
            
    Clubs= cursor.fetchall()

    if not Clubs: return Response({'Message':"No Club Exist"})

    json_data = [dict(zip(CityCols, row)) for row in Clubs]

    return Response(json_data)

@api_view(['POST'])
def ClubByCity(request):
            
    data= JSONParser().parse(request)

    cursor.execute('SELECT ClubName \
                    From Club c inner join Stadium  s \
                    on c.StadiumName= s.StadiumName  \
                    where s.City= %s;', (data['City'],))
            
    Clubs= cursor.fetchall()

    if not Clubs: return Response([{'Message':"No Club Exist"}])

    json_data = [dict(zip(['ClubName'], row)) for row in Clubs]

    return Response(json_data)

@api_view(['POST'])
def ClubByStadium(request):
            
    data= JSONParser().parse(request)

    cursor.execute('SELECT ClubName \
                    From Club c inner join Stadium  s \
                    on c.StadiumName= s.StadiumName  \
                    where c.StadiumName= %s;', (data['StadiumName'],))
            
    Clubs= cursor.fetchall()

    if not Clubs: return Response([{'Message':"No Club Exist"}])

    json_data = [dict(zip(['ClubName'], row)) for row in Clubs]

    return Response(json_data)

#####################################################################
##Top Teams
@api_view(['GET'])
def MostWonBySeason(request):

    cursor.execute("Create OR REPLACE View allWin As \
                    SELECT ClubName, Season, SUM(CASE\
                    WHEN ClubName = Home_ClubName AND Home_Goals > Away_Goals THEN 1\
                    WHEN ClubName = Away_ClubName AND Home_Goals < Away_Goals THEN 1\
                    ELSE 0\
                    END) AS WIN\
                    FROM Club Inner JOIN MatchGame \
                    ON ClubName = Home_ClubName OR ClubName = Away_ClubName\
                    GROUP BY Season, ClubName\
                    ORDER BY WIN DESC;")

    cursor.fetchall()
    cursor.execute("Select ClubName, Season, WIN \
                    from allWin \
                    Where (Season, WIN) In ( \
                    Select Season, max(WIN) \
                    from allWin \
                    Group By Season) \
                    Order by Season;")

    Wins= cursor.fetchall()

    ColTitles=['Season', 'ClubName', 'NumberOfWins']

    json_data = [dict(zip(ColTitles, row)) for row in Wins]

    return Response(json_data)

@api_view(['GET'])
def TotalWins(request):
            
    cursor.execute('Select c.ClubName as Club, Home_wins+ Away_wins as WinningGames\
                    From Club c left join(\
	                    Select Home_ClubName,  COUNT(*) AS Home_wins\
	                    From MatchGame\
	                    Where Home_Goals > Away_Goals\
	                    Group By Home_ClubName) HomeW\
                    ON HomeW.Home_ClubName = c.ClubName\
                    left join(\
	                    Select Away_ClubName,  COUNT(*) AS Away_wins\
	                    From MatchGame\
	                    Where Home_Goals < Away_Goals\
	                    Group By Away_ClubName) AwayW\
                        ON AwayW.Away_ClubName = c.ClubName\
                        ORDER BY WinningGames DESC\
                        Limit 10;')
            
    Wins= cursor.fetchall()

    ColTitles=['Club', 'WinningGames']

    json_data = [dict(zip(ColTitles, row)) for row in Wins]

    return Response(json_data)

@api_view(['GET'])
def TotalHomeWins(request):
            
    cursor.execute('Select c.ClubName as Club, Home_Matches_Won\
                    From Club c left join(\
	                    Select Home_ClubName,  COUNT(*) AS Home_Matches_Won\
	                    From MatchGame\
	                    Where Home_Goals > Away_Goals\
	                    Group By Home_ClubName) HomeW\
                    ON HomeW.Home_ClubName = c.ClubName\
                    ORDER BY Home_Matches_Won DESC\
                    Limit 10;')
            
    Wins= cursor.fetchall()

    ColTitles=['Club', 'WinningGames']

    json_data = [dict(zip(ColTitles, row)) for row in Wins]

    return Response(json_data)

@api_view(['GET'])
def TotalYellowCards(request):
            
    cursor.execute('Select c.ClubName as Club,Home_yellow+ Away_yellow as Yellow_Cards \
                    From Club c left join(\
	                    Select Home_ClubName,  sum(Home_YellowCards) AS Home_yellow\
	                    From MatchGame\
	                    Group By Home_ClubName) HomeY\
                    ON HomeY.Home_ClubName = c.ClubName\
                    left join(\
	                    Select Away_ClubName,  sum(Away_YellowCards) AS Away_yellow\
	                    From MatchGame\
	                    Group By Away_ClubName) AwayY\
                    ON AwayY.Away_ClubName = c.ClubName\
                    ORDER BY Yellow_Cards DESC\
                    Limit 10;')
            
    Wins= cursor.fetchall()

    ColTitles=['Club', 'YellowCardsNumber']

    json_data = [dict(zip(ColTitles, row)) for row in Wins]

    return Response(json_data)

@api_view(['GET'])
def TotalFouls(request):
            
    cursor.execute('Select c.ClubName as Club, Home_fouls+ Away_fouls as Fouls\
                    From Club c left join(\
	                    Select Home_ClubName,  sum(Home_Fouls) AS Home_fouls\
	                    From MatchGame\
	                    Group By Home_ClubName) HomeF\
                    ON HomeF.Home_ClubName = c.ClubName\
                    left join(\
	                    Select Away_ClubName,  sum(Away_Fouls) AS Away_fouls\
	                    From MatchGame\
	                    Group By Away_ClubName) AwayF\
                    ON AwayF.Away_ClubName = c.ClubName\
                    ORDER BY Fouls DESC\
                    Limit 10;')
            
    Wins= cursor.fetchall()

    ColTitles=['Club', 'FoulsNumber']

    json_data = [dict(zip(ColTitles, row)) for row in Wins]

    return Response(json_data)

@api_view(['GET'])
def Totalshots(request):
            
    cursor.execute('Select c.ClubName as Club, Home_shots+ Away_shots as Shots\
                    From Club c left join(\
	                    Select Home_ClubName,  sum(Home_Shots) AS Home_shots\
	                    From MatchGame\
	                    Group By Home_ClubName) HomeSh\
                    ON HomeSh.Home_ClubName = c.ClubName\
                    left join(\
	                    Select Away_ClubName,  sum(Away_Shots) AS Away_shots\
	                    From MatchGame\
	                    Group By Away_ClubName) AwaySh\
                    ON AwaySh.Away_ClubName = c.ClubName\
                    ORDER BY Shots DESC\
                    Limit 10;')
            
    Wins= cursor.fetchall()

    ColTitles=['Club', 'ShotsNumber']

    json_data = [dict(zip(ColTitles, row)) for row in Wins]

    return Response(json_data)
##################################################################









