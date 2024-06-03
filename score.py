from utils import SCORES_FILE_NAME
from app import game_level

def add_score():
    score_add = game_level*3+5
    f = open(SCORES_FILE_NAME, "r")
    file_score = f.read()
    f.close()
    score_add = score_add+int(file_score)
    ##overide the file ##
    f = open(SCORES_FILE_NAME, "w")
    f.write(score_add)
    f.close()
    
