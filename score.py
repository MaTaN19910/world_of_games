from utils import SCORES_FILE_NAME
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
    score_add = score_add+int(old_score)
    ##overide the file ##
    f = open(SCORES_FILE_NAME, "w")
    f.write(str(score_add))
    f.close()
    
