from difflib import Match
from lib2to3.pgen2 import driver
from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import pandas as pd
import numpy as np
import ast



def launchWebpage(url):
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
        
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe", options=options)
    driver.set_window_size(1120, 1000)

    driver.get(url)
    timeout = 10
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Accept All Cookies']")))
    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.quit()
    return driver

def scrollDown(driver):
    # Scroll down
    current_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 	# Scroll step
        time.sleep(5) 	# Wait to load page
        try:
            new_height = driver.execute_script("return document.body.scrollHeight") # Calculate new scroll height
        except:
            print("Failed: ", new_height)
        if new_height == current_height: # Compare with last scroll height
            break
        current_height = new_height

    print("scorlled till",current_height)


def getResults(driver):
    
    time.sleep(3)
    Matches_wait= WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Results")))
    driver.execute_script("arguments[0].click();", Matches_wait)

    #Past four seasons without the current one included
    gameLinks=[]
    
    gameSeason=[]

    for i in range(1,5):

        driver.execute_script("window.scrollTo(0, 0);")
        
        time.sleep(3)
        
        Filter= WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mainContent']/div[3]/div[1]/section/div[3]/div[2]")))
        
        
        driver.execute_script("arguments[0].click();", Filter)
        
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mainContent']/div[3]/div[1]/section/div[3]/ul/li["+str(i)+"]")))
        
        except TimeoutException:
            print("Timed out waiting for page to load")
            driver.quit()
        
        Season= driver.find_element_by_xpath("//*[@id='mainContent']/div[3]/div[1]/section/div[3]/ul/li["+str(i)+"]")
         
        Season.click()

        time.sleep(5)

                
        scrollDown(driver)
        
        
        GS=Season.text        
        
        Games= driver.find_elements(By.CSS_SELECTOR,"div[class='fixture postMatch']")
       
        for j in range(len(Games)):
            
            gameLinks.append("https://"+ Games[j].get_attribute("data-href")[2:])
            
            gameSeason.append(GS)

    MatchGames=[]
    
    print(len(set(gameLinks)))

    for game in range(len(gameLinks)):
       
        driver.get(gameLinks[game])

        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[class='matchDate renderMatchDateContainer']")))
        except TimeoutException:
            print("Timed out waiting for page to load")
            driver.quit()
              
        MatchDate = driver.find_element(By.CSS_SELECTOR,"div[class='matchDate renderMatchDateContainer']").text
        
        StadiumName = driver.find_element(By.CSS_SELECTOR,"div[class='stadium']").text
        
        StadiumName= StadiumName[:StadiumName.rindex(',')]
        
        homeTeam= driver.find_element(By.CSS_SELECTOR,"div[class='team home']").text
        
        awayTeam= driver.find_element(By.CSS_SELECTOR,"div[class='team away']").text
        
        score= driver.find_element(By.CSS_SELECTOR,"div[class='score fullTime']").text
        
        Home_Goals= score[0]
        
        Away_Goals=score[2]

                
        stats= WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mainContent']/div/section[2]/div[2]/div[2]/div[1]/div/div/ul/li[3]")))
        
        driver.execute_script("arguments[0].click();", stats)

        conc={"Home_Yellow":0, "Home_Red":0, "Home_Fouls":0, 
              "Away_Yellow":0, "Away_Red":0, "Away_Fouls":0,  }
        
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='mainContent']/div/section[2]/div[2]/div[2]/div[2]/section[3]/div[2]/div[2]/table/tbody/tr")))
        except TimeoutException:
            print("Timed out waiting for page to load")
            driver.quit()
              

        S1 = driver.find_elements_by_xpath("//*[@id='mainContent']/div/section[2]/div[2]/div[2]/div[2]/section[3]/div[2]/div[2]/table/tbody/tr")
        
      
        for row in range(len(S1)):
            S1_list = S1[row].text.split() 
            S1_name= S1_list[1]
            conc["Home_" + S1_name] = float(S1_list[0])
            conc["Away_" + S1_name] = float(S1_list[-1])

        game_dict = {
		"StadiumName": StadiumName,
		"Home_ClubName": homeTeam,
		"Away_ClubName": awayTeam,
        "MatchDate": MatchDate,
        "Home_Goals": Home_Goals, 
	    "Home_Possession %": conc["Home_Possession"], 
        "Home_YellowCards": int(conc["Home_Yellow"]) ,
        "Home_RedCards": int(conc["Home_Red"]) , 
        "Home_Fouls": int(conc["Home_Fouls"]) , 
        "Home_Shots": int(conc["Home_Shots"]) ,
        "Away_Goals":Away_Goals , 
	    "Away_Possession %": conc["Away_Possession"], 
        "Away_YellowCards": int(conc["Away_Yellow"]) ,
	    "Away_RedCards": int(conc["Away_Red"]) , 
        "Away_Fouls": int(conc["Away_Fouls"]) , 
        "Away_Shots": int(conc["Away_Shots"])
	    }
        print(game_dict)
        MatchGames.append(game_dict)
        print(len(MatchGames))

    df = pd.DataFrame(MatchGames)
    df.insert(loc=0, column='Game_Season', value=gameSeason)

    df.to_csv('MatchGames.csv',index=True)


def getClubs(driver):
    
    time.sleep(3)
    Clubs_wait= WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Clubs")))
    driver.execute_script("arguments[0].click();", Clubs_wait)

    ClubsDict={}
    for i in range(1,5):

        driver.execute_script("window.scrollTo(0, 0);")
        
        time.sleep(3)
        
        seasons_club= WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mainContent']/div[2]/div/section/div[1]/div[2]")))
        
        driver.execute_script("arguments[0].click();", seasons_club)

        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mainContent']/div[2]/div/section/div[1]/ul/li["+str(i)+"]")))
        except TimeoutException:
            print("Timed out waiting for page to load")
            driver.quit()
        
        Season= driver.find_element_by_xpath("//*[@id='mainContent']/div[2]/div/section/div[1]/ul/li["+str(i)+"]")
         
        Season.click()
        
        time.sleep(5)
        
        scrollDown(driver)
        
        Clubs= driver.find_elements_by_xpath(" //*[@id='mainContent']/div[2]/div/div/div[1]/div/ul/li/a")
        ClubNames = driver.find_elements_by_class_name("clubName")
        StadiumNames= driver.find_elements_by_class_name("stadiumName")

        for c in range(len(Clubs)):
            if ClubNames[c].text== "Tottenham Hotspur" and "Tottenham Hotspur" in ClubsDict:
                continue
            clubInfo= [StadiumNames[c].text, Clubs[c].get_attribute('href')]
            ClubsDict[ClubNames[c].text]=clubInfo

    AllClubs=[]
    Websites=[]
    Stadiums=[]

    StadiumLinks=[]
    for club, clubInfo in ClubsDict.items():
        AllClubs.append(club)
        Stadiums.append(clubInfo[0])
        driver.get(clubInfo[1])
        Websites.append(driver.find_element_by_xpath("//*[@id='mainContent']/header/div[2]/div/div/div[2]/div[2]/a").text)
        StadiumLinks.append([clubInfo[0],driver.find_element_by_xpath("//*[@id='mainContent']/nav/ul/li[7]/a").get_attribute('href')])
    
    finalClubDict={
        'ClubName':AllClubs,
        'CurrentStadium':Stadiums,
        'Website':Websites
    }    
    df = pd.DataFrame(finalClubDict)
    df['StadiumLinks']= StadiumLinks
    df.to_csv('Clubs.csv',index=True)


def getStadiums(driver):

    df= pd.read_csv('Clubs.csv')
    
    StadiumLinks=list(df['StadiumLinks'])

    StadiumDF=[]
    
    for row in StadiumLinks:

        stadiumDict={'Capacity:': 'NULL', 'Record': 'NULL', 'Built:': 'NULL',
                     'Pitch': 'NULL', 'Stadium':'NULL' }

        row= ast.literal_eval(row)
        
        stadiumName= row[0]
        
        stadiumLink=row[1]
        
        print(stadiumLink)
        
        driver.get(stadiumLink)
        
        Info= driver.find_elements_by_xpath("//*[@id='mainContent']/div[3]/div[3]/div[2]/p")
        
        StadiumInfo={}

        for inf in range(len(Info)):
            try:
                Info[inf].get_attribute('textContent').split()[0]
            except IndexError:
                break
            if (Info[inf].get_attribute('textContent').split()[0] == 'Stadium'):
                stadiumDict[Info[inf].get_attribute('textContent').split()[0]]= Info[inf].get_attribute('textContent').split(sep=',')
            else:
                stadiumDict[Info[inf].get_attribute('textContent').split()[0]]= Info[inf].get_attribute('textContent').split()
        

        StadiumInfo['StadiumName']= stadiumName

        StadiumInfo ['City'] = stadiumDict['Stadium'][-2][1:] if len(stadiumDict['Stadium'])<5 else stadiumDict['Stadium'][-3][1:]
        
        StadiumInfo ['Street'] = stadiumDict['Stadium'][1][1:]
        
        StadiumInfo['Postcode'] = stadiumDict['Stadium'][-1][1:]

        if stadiumDict['Capacity:']!='NULL':
            StadiumInfo['Capacity']= int("".join((stadiumDict['Capacity:'][1]).split(sep=',')))
        else: StadiumInfo['Capacity']='NULL'

        StadiumInfo['BuildingDate'] = stadiumDict['Built:'][1] 

        StadiumInfo['PitchLength']= float(stadiumDict['Pitch'][2][:-1])
        
        StadiumInfo['PitchWidth']= float(stadiumDict['Pitch'][4][:-1])

        if stadiumDict['Record']!='NULL':
            StadiumInfo['RecordLeagueAttendance']= int("".join((stadiumDict['Record'][3]).split(sep=','))) 
        else: StadiumInfo['RecordLeagueAttendance']='NULL'

        StadiumDF.append(StadiumInfo)

    df = pd.DataFrame(StadiumDF)
    df.to_csv('Stadiums.csv',index=True)



def getOtherPlayers(driver, PlayerDict, AllPlayerClubR):

    dict={}

    driver.get('https://www.premierleague.com/players')

    time.sleep(3)
        
    scrollDown(driver)

    Player=driver.find_elements_by_class_name ("playerName")
            
    PlayerPosition=driver.find_elements_by_xpath ("//*[@id='mainContent']/div[2]/div/div/div/table/tbody/tr/td[2]")
            
    PlayerCountry= driver.find_elements_by_class_name ("playerCountry")

    print(len(Player))

    for p in range(len(Player)):
            
        Name= Player[p].text

        if not ",".join([Name, Player[p].get_attribute('href')]) in PlayerDict.keys():
            PlayerDict[",".join([Name, Player[p].get_attribute('href')])]=[PlayerPosition[p].text,PlayerCountry[p].text]
            dict [",".join([Name, Player[p].get_attribute('href')])]=1
        else:
            pass
    
    for Player, PlayerMainInfo in dict.items():
        
        driver.get(Player.split(sep=',')[1])

        isPresent = len(driver.find_elements(By.CLASS_NAME, "team")) > 0

        if isPresent:
            ClubName = driver.find_element_by_class_name("team").text
        else:
             ClubName = 'NULL'

        PlayerForClub={"ClubName": ClubName, "PlayerName":Player.split(sep=',')[0],"DateOfBirth":'NULL', "Season":'2021/22' }

        AllPlayerClubR.append(PlayerForClub)

        print(len(AllPlayerClubR))

        print("Other",AllPlayerClubR[-1])




def getPlayer_Club(driver):
    
    time.sleep(3)
    
    Players_wait= WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Players")))
    
    driver.execute_script("arguments[0].click();", Players_wait)

    PlayerDict={}

    AllPlayers=[]

    AllPlayerClubR=[]
    
    for i in range(1,5):

        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)
        seasons_player= WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mainContent']/div[2]/div[1]/div/section/div[1]/div[2]")))
        driver.execute_script("arguments[0].click();", seasons_player)
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mainContent']/div[2]/div[1]/div/section/div[1]/ul/li["+str(i)+"]")))
        
        except TimeoutException:
            print("Timed out waiting for page to load")
            driver.quit()
        Season= driver.find_element_by_xpath("//*[@id='mainContent']/div[2]/div[1]/div/section/div[1]/ul/li["+str(i)+"]")
        
        time.sleep(5)
        
        GS=Season.text
        
        Season.click()

        for j in range (2,22):
            
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(3)
            Clubs_player= WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mainContent']/div[2]/div[1]/div/section/div[2]/div[2]")))
            driver.execute_script("arguments[0].click();", Clubs_player)
            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mainContent']/div[2]/div[1]/div/section/div[2]/ul/li["+str(j)+"]")))
            
            except TimeoutException:
                print("Timed out waiting for page to load")
                driver.quit()            
            
            ClubClick= WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mainContent']/div[2]/div[1]/div/section/div[2]/ul/li["+str(j)+"]")))
            
            ClubName= driver.find_element_by_xpath("//*[@id='mainContent']/div[2]/div[1]/div/section/div[2]/ul/li["+str(j)+"]").text
            
            driver.execute_script("arguments[0].click();", ClubClick)
            
            scrollDown(driver)

            Player=driver.find_elements_by_class_name ("playerName")
            
            PlayerPosition=driver.find_elements_by_xpath ("//*[@id='mainContent']/div[2]/div/div/div/table/tbody/tr/td[2]")
            
            PlayerCountry= driver.find_elements_by_class_name ("playerCountry")

            for p in range(len(Player)):
            
                Name= Player[p].text
                
                PlayerDict[",".join([Name, Player[p].get_attribute('href')])]=[PlayerPosition[p].text,PlayerCountry[p].text]

                PlayerForClub={"ClubName": ClubName, "PlayerName":Name,"DateOfBirth":'NULL', "Season":GS }

                AllPlayerClubR.append(PlayerForClub)

                print(len(AllPlayerClubR))

                print(AllPlayerClubR[-1])

    getOtherPlayers(driver, PlayerDict, AllPlayerClubR)
    
    PlayerClubDf = pd.DataFrame(AllPlayerClubR)

    PlayerClubDf.to_csv('PlayerClubNOBD.csv')

    for Player, PlayerMainInfo in PlayerDict.items():

        PlayerInfo={'PlayerName': 'NULL', 'DateOfBirth': 'NULL', 'Nationality':'NULL', 'Weight Kg':'NULL',
                        'Height Cm': 'NULL', 'PlayingPosition':'NULL'}
                
        PlayerInfo['PlayerName']= Player.split(sep=',')[0]
                
        PlayerInfo['PlayingPosition']= PlayerMainInfo[0]
                
        PlayerInfo['Nationality']= PlayerMainInfo[1]
                
        driver.get(Player.split(sep=',')[1])

        PlayerInfoTable= driver.find_elements_by_xpath("//*[@id='mainContent']/div[3]/div/div/div[1]/section/div/ul/li")
                
        table={'Date': 'NULL', 'Height':'NULL', 'Weight': 'NULL'}
                
        for pi in range(len(PlayerInfoTable)):

            l=PlayerInfoTable[pi].get_attribute('textContent').split()

            try: l[0]
            except IndexError: continue

            table[l[0]]= l[-1]
                    
            if l[0]=='Date': table[l[0]]= l[3]

        PlayerInfo['DateOfBirth']=table['Date']

        PlayerInfo['Height Cm']=float(table['Height'][:-2]) if table['Height']!= 'NULL' else 'NULL'
                
        PlayerInfo['Weight Kg']= float(table['Weight'][:-2]) if table['Weight']!= 'NULL' else 'NULL'

        AllPlayers.append(PlayerInfo)
                
        print(len(AllPlayers))
                
        print(AllPlayers[-1])
            
    df = pd.DataFrame(AllPlayers)
            
    df.to_csv('Players.csv',index=True)
    
    PlayerClubDf.to_csv('PlayerClub.csv')
    

if __name__ == "__main__":
    

    driver= launchWebpage("https://www.premierleague.com")
    cookie_button = driver.find_element_by_xpath("//button[text()='Accept All Cookies']")
    cookie_button.click()
    
    #Scraping Matches for the past 4 seasons "Results"
    getResults(driver)

    #Scraping Clubs of the past 4 seasons
    driver.get("https://www.premierleague.com")
    getClubs(driver)

    
    #Scraping Stadiums of the past 4 seasons
    driver.get("https://www.premierleague.com")
    getStadiums(driver)

    #Scraping Players Clubs table of the past 4 seasons
    driver.get("https://www.premierleague.com")
    getPlayer_Club(driver)

