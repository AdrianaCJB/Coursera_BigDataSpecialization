You can export the result of MongoDB queries using the mongoexport command in the terminal shell. 
This command uses the following arguments:

The mongoexport file is located in /big-data-3/mongodb/bin/. The format of the command is as follows:

./bin/mongoexport --db <dbname> --collection <collectionName> --out <OutfileName>

Your assignment is to export user data from the sample db to any output file.

	Argument										Description
--collection <name>								The collection to use.
--db <name>										The database to use.
--fields <field 1>,<field 2>,<...>				The fields to include in the query result.
--query <query>									The query to perform.
--out <name>									The name of the output file.
--type=<type>									Format of export, either csv or json.


Assignment: Querying and Exporting from MongoDB
'''Imagine you are the Sports Analyst for a big magazine. The goal of this assignment 
is to demonstrate your data-driven reporting skills and express the following natural 
language questions as MongoDB queries on soccer-related tweets in English.'''

# start MongoDB server
cd Downloads/big-data-3/mongodb
./mongodb/bin/mongod --dbpath db

# open a new terminal shell window, start MongoDB shell
cd Downloads/big-data-3/mongodb
./mongodb/bin/mongo
Query 1: How many tweets have location not null?

db.users.find({"user.Location": {$ne: null}}).count()
# 6937
Query 2: How many people have more followers than friends?

db.users.find({
    $where: "this.user.FollowersCount > this.user.FriendsCount"
}).count()
# 5809
Query 3: Return text of tweets which have the string "http://" ?

db.users.find({$text: {$search: "http://"}}, {tweet_text: 1, _id: 0})
Query 4: Return all the tweets which contain text "England" but not "UEFA" ?

db.users.find({$text: {$search: "England - UEFA"}}, {tweet_text: 1, _id: 0})
Query 5: Get all the tweets from the location "Ireland" and contains the string "UEFA"?

db.users.find({
    $and: [
        {"user.Location": {$eq: "Ireland"}},
        {tweer_text: /UEFA/}
        ]
    }, {"user.FriendsCount": 1})

# results as following
# {"_id": ObjectId("578ffc547eb951401527b5da"), "user": {"FriendsCount": 2381}}
# {"_id": ObjectId("578ffda17eb951401527b738"), "user": {"FriendsCount": 2277}}
# {"_id": ObjectId("57965ef5c38159118f94f8ae"), "user": {"FriendsCount": 802}}
# {"_id": ObjectId("57966dc0c38159201ca7f637"), "user": {"FriendsCount": 0}}

# then, in order to find the user with the highest "FriendsCount", we can code:
db.users.find({_id: ObjectId("578ffc547eb951401527b5da")}, {user_name: 1})
# the user "ProfitwatchInfo" has the highest "FriendsCount"

----------------------------------------------------------------------------

Game " Catch The Pink Flamingo "

Tables:

users
 (userID:longInteger, userName:string, joiningDate:date, dateOfBirth:date, currentLevel:int, authenticationKey:string )
 
teams
(teamID:longInteger, userID:longInteger, teamName:string, joiningDate:date, dateDelete:date, archived:bool)

map
(mapID: longInteger, mapComplexity: string)

level 
(levelID: longInteger, complexity: string )

mission
(misionID:longInteger, description:string, mapID: longInteger, speed: int,
missionFreeze: bool)

missions_levels
(misionLevelID: longInteger, levelID: longInteger, missionID:longInteger )

user_mission
( userID:longInteger, currentMissionLevelID:longInteger, points: Integer)

chat_board
( chatID:longInteger , userID:longInteger, message: string)

ranking_user # Each user will be ranked individually
(userID:longInteger, puntuation: Integer, velocity: Integer, accuracy: Integer, clasification:string)

ranking_team # The teams are ranked publicly
(teamID:longInteger, votation:Integer) 

purchases_game
( userID:longInteger, itemID: longInteger, missionID:longInteger)





























