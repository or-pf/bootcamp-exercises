import pymysql
from pymysql import connect, cursors
actors = ["Richard Gear", "Simon Pegg", "Zach Braff"]

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="imdb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor)

def find_actors(actors_list):
    try:
        with connection.cursor() as cursor:
            sql= "select full_name from actors"
            cursor.execute(sql)
            result= cursor.fetchall()
            full_names_list= [actor["full_name"] for actor in result]
            for actor in actors_list:
                if actor in full_names_list:
                    print (f"the actor {actor} is in the DB")
                else:
                    print (f"the actor {actor} isn't in the imbd database")
    except:
         print('something went wrong with the connection to the db')

def main():
    find_actors(actors)


if __name__ == '__main__':
    main()