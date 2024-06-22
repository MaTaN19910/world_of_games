from flask import Flask 
from flask import render_template 
file_flag = False
"""
read the score from Scores file
"""
def get_score():
    try:
        f = open("Scores.txt")
    except IOError:
        file_flag=True
    score= f.read()
    f.close()
    return score

  
# creates a Flask application 
app = Flask(__name__) 
  
  
@app.route("/") 
def hello(): 

    return render_template('index.html',  SCORE=get_score()) 
## all error htmls
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html'), 500

@app.errorhandler(400)
def page_not_found(e):
    return render_template('error.html'), 400




# run the application 
if __name__ == "__main__": 
    if file_flag == False:
        app.run(host="0.0.0.0", port=int(5000) ,debug=True)
    else:
        app.run(page_not_found)
