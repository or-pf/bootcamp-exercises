import pymysql
from pymysql import connect, cursors

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="imdb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor)

actors = ({'id': 654321, 'full_name': 'daniel day-lewis', 'gender': 'M'},
          {'id': 325814, 'full_name': 'Oscar Isaac', 'gender': 'M'},
          {'id': 666662, 'full_name': 'Scarlett Johansson', 'gender': 'F'},
          {'id': 22591, 'full_name': 'Kevin Bacon', 'gender': 'M'},
          {'id': 684312, 'full_name': 'Olivia Wilde', 'gender': 'F'},
          {'id': 684355, 'full_name': 'test adding', 'gender': 'M'})


def add_actors(actors):
    with connection.cursor() as cursor:
        
        for actor in actors:
            sql = "insert into actors (id, full_name, gender) values (%d, '%s', '%s')" % (actor["id"], actor["full_name"], actor["gender"])
            try:
                # print(sql)
                cursor.execute(sql)
                connection.commit()
                print("the actor " + actor["full_name"] +" was added to DB")
                
            except:
                cursor.execute(f"SELECT * FROM actors where id={actor['id']}")
                row = cursor.fetchone()
                if row is not None:
                    print("the actor " + actor["full_name"] +" is already in the DB")

def main():
    add_actors(actors)


if __name__ == '__main__':
    main()
