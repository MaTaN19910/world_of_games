import os,time
"""
This file will init the Scores.txt file and clear the screen func
"""
SCORES_FILE_NAME = "Scores.txt"

BAD_RETURN_CODE = 0



def Screen_cleaner():
    time.sleep(1)
    os.system('clear')

def init_score():
    f = open(SCORES_FILE_NAME, "w")
    f.write("0")
    f.close()

