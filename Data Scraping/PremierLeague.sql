CREATE SCHEMA IF NOT EXISTS `PremiurLeague` ;
USE `PremiurLeague`;

Show variables like "local_infile";

set global local_infile = 1;

CREATE TABLE IF NOT EXISTS Stadium(
	StadiumName varchar(50) NOT NULL PRIMARY KEY, 
    City varchar(20) NOT NULL, 
    Street varchar(40),
    Postcode varchar(10),
	Capacity int, 
    BuildingDate char(4), 
    PitchLength float NOT NULL, 
    PitchWidth float NOT NULL,
    RecordLeagueAttendance int
);
LOAD DATA LOCAL INFILE "C:\\Users\\Abdelrahman\\Desktop\\DB Project PH2\\Stadiums.csv" 
INTO TABLE Stadium
CHARACTER SET euckr 
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

CREATE TABLE IF NOT EXISTS Player(
	PlayerName varchar(50) NOT NULL, 
    DateOfBirth DATE NOT NULL, 
    Nationality varchar(20), 
    Weight float, 
    Height float,
    PlayingPosition varchar(20) NOT NULL, 
	PRIMARY KEY (PlayerName, DateOfBirth)
);

LOAD DATA LOCAL INFILE "C:\\Users\\Abdelrahman\\Desktop\\DB Project PH2\\Players_Data.csv"
INTO TABLE Player
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

CREATE TABLE IF NOT EXISTS Club(
	ClubName varchar(50) NOT NULL PRIMARY KEY, 
    StadiumName varchar(50) NOT NULL, 
    Website varchar(100) NOT NULL,
    constraint FK_ClubStd FOREIGN KEY (StadiumName) REFERENCES Stadium (StadiumName)
    ON UPDATE CASCADE 
    ON DELETE CASCADE
);

LOAD DATA LOCAL INFILE "C:\\Users\\Abdelrahman\\Desktop\\DB Project PH2\\Clubs.csv"
INTO TABLE Club
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

CREATE TABLE IF NOT EXISTS PlayerForClub(
	P_ClubName varchar(50) NOT NULL,
	Player_Name varchar(50) NOT NULL,
    BD DATE NOT NULL, 
    Season char(7) NOT NULL, 
    PRIMARY KEY (ClubName, PlayerName, DateOfBirth, Season),
    CONSTRAINT FK_Player FOREIGN KEY (Player_Name, BD)
    REFERENCES Player (PlayerName, DateOfBirth)
	ON UPDATE CASCADE ON DELETE CASCADE ,
    CONSTRAINT FK_Club FOREIGN KEY(P_ClubName) 
    REFERENCES Club(ClubName)
    ON UPDATE CASCADE ON DELETE RESTRICT
);

LOAD DATA LOCAL INFILE "C:\\Users\\Abdelrahman\\Desktop\\DB Project PH2\\PlayersClubs.csv"
INTO TABLE PlayerForClub
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

CREATE TABLE IF NOT EXISTS MatchGame(
	Season char(7) NOT NULL, 
	Home_ClubName varchar(50) NOT NULL,
	Away_ClubName varchar(50) NOT NULL,
	MatchDate date NOT NULL,
	Home_Goals int NOT NULL, 
	Home_Possession float NOT NULL, 
    Home_YellowCards int ,
	Home_RedCards int , 
    Home_Fouls int , 
    Home_Shots int , 
   	Away_Goals int NOT NULL, 
	Away_Possession float NOT NULL, 
    Away_YellowCards int ,
	Away_RedCards int , 
    Away_Fouls int , 
    Away_Shots int , 
    PRIMARY KEY (MatchDate, Home_ClubName, Away_ClubName),
    constraint FK_Match_Home_Club FOREIGN KEY(Home_ClubName) REFERENCES Club(ClubName)
    ON UPDATE CASCADE ON DELETE RESTRICT ,
    constraint FK_Match_Away_Club FOREIGN KEY(Away_ClubName) REFERENCES Club(ClubName)
    ON UPDATE CASCADE ON DELETE RESTRICT 
);

LOAD DATA LOCAL INFILE "C:\\Users\\Abdelrahman\\Desktop\\DB Project PH2\\Matches_Data.csv"
INTO TABLE MatchGame
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

CREATE TABLE IF NOT EXISTS FanUser(
	UserEmail varchar(50) NOT NULL PRIMARY KEY, 
    UserName  varchar(50),
    Gender    char(1) NOT NULL,
    DateOfBirth   date NOT NULL,
    FavouriteClubName varchar(50) NOT NULL, 
    constraint FK_Club_Fan FOREIGN KEY (FavouriteClubName) REFERENCES Club(ClubName)
    ON UPDATE CASCADE ON DELETE RESTRICT 
);


CREATE TABLE IF NOT EXISTS FanUserMatchReview(
	UserEmail varchar(50) NOT NULL, 
    MatchDate date NOT NULL, 
	Home_ClubName varchar(50) NOT NULL,
	Away_ClubName varchar(50) NOT NULL,
	Rate decimal(3,1) NOT NULL,
    TextReview  varchar(2000) NOT NULL, 
    PRIMARY KEY (UserEmail, MatchDate, Home_ClubName, Away_ClubName), 
	CONSTRAINT FK_MatchDate FOREIGN KEY (MatchDate) REFERENCES MatchGame (MatchDate)
	ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_UserEmail FOREIGN KEY (UserEmail) REFERENCES FanUser(UserEmail)
	ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_Home_ClubName FOREIGN KEY (Home_ClubName) REFERENCES Club (ClubName)
	ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_Away_ClubName FOREIGN KEY (Away_ClubName) REFERENCES Club (ClubName)
    ON UPDATE CASCADE ON DELETE CASCADE
);

DELETE FROM FanUserMatchReview;

LOAD DATA LOCAL INFILE "C:\\Users\\Abdelrahman\\Desktop\\DB Project PH2\\Reviews.csv"
INTO TABLE FanUserMatchReview
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;