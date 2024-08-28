from utils import SCORES_FILE_NAME
from db_pass import POSTGRESS_PASS
import asyncio
import asyncpg

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
#    add_value_to_db()
    asyncio.run(add_value_to_db())

async def add_value_to_db():
    value= read_value_from_text()
    connection = await asyncpg.connect(user='postgres',password=POSTGRESS_PASS,database='postgres',host='localhost')
    await connection.execute("INSERT INTO users_scores (score) VALUES ($1)", value)
    await connection.close()



def read_value_from_text():
    with open(SCORES_FILE_NAME, 'r') as file:
        value = file.read().strip()


    # score_add = score_add+int(old_score)
    # ##overide the file ##
    # f = open(SCORES_FILE_NAME, "w")
    # f.write(str(score_add))
    # f.close()
    
