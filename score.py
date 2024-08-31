from utils import SCORES_FILE_NAME
from db_pass import POSTGRESS_PASS
import psycopg2
"""
This func will get the old score from the file
"""
def get_old_score():
    f = open(SCORES_FILE_NAME, "r")
    old_score = f.read()
    f.close
    return old_score

"""
this func will set the new score in Scores.txt file
"""
def add_score(game_level_input):
    old_score = get_old_score()
    score_add = game_level_input*3+5
    score= int(old_score)+int(score_add)
    f = open(SCORES_FILE_NAME, "w")
    f.write(str(score))
    f.close()
    insert_score(score)



## this funx will add the value to db ##
def insert_score(score):
    try:
        # Connect to your PostgreSQL database
        connection = psycopg2.connect(
            user="postgres",
            password=POSTGRESS_PASS,
            host="localhost",
            port="5432",
            database="postgres"
        )
        cursor = connection.cursor()

        # Insert a value into the score column
        insert_query = """INSERT INTO users_scores (score) VALUES (%s);"""
        cursor.execute(insert_query, (score,))

        # Commit the transaction
        connection.commit()

        print("Value inserted successfully")

    except (Exception, psycopg2.Error) as error:
        print("Error while inserting data", error)

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    
