import pymysql
from pymysql import connect, cursors

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="imdb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True)

def add_column_num_of_movies(): 
    with connection.cursor() as cursor:
        
        try:
# to add an empty column:

            # alterStatement = "ALTER TABLE actors ADD num_of_movies int(5)"
            # cursor.execute(alterStatement)

# to check if a column was created:

            # descibeStatement  = "DESC actors"
            # cursor.execute(descibeStatement)
            # columns = cursor.fetchall()
            # for column in columns:
            #     print(column)     


            selectStatement= "select count(actor_id), actor_id from cast group by actor_id" 
            cursor.execute(selectStatement)
            num_of_movies_list = cursor.fetchall()
            # print(num_of_movies_list)

            for i in num_of_movies_list:
                insertStatement = "update actors set num_of_movies={} where id={}"
                cursor.execute(insertStatement.format(i['count(actor_id)'], i['actor_id']))


 
        except Exception as e:
            print("Exeception occured:{}".format(e))


def main():
    add_column_num_of_movies()


if __name__ == '__main__':
    main()
