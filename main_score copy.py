from flask import Flask, render_template, request, redirect, url_for
from score import add_score
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
def intro(): 

    return render_template('intro.html',  SCORE=get_score()) 
## all error htmls
@app.route('/gamepicker')
def gamepicker():
    level = request.args.get('level')
    return render_template('gamepicker.html', level=level)

@app.route('/play/<game>')
def play(game):
    level = request.args.get('level')
    if game == 'currency_roulette_game':
        return redirect(f"http://localhost:5001?level={level}")
    elif game == 'guess_game':
        return redirect(f"http://localhost:5002?level={level}")
    elif game == 'memory_game':
        return redirect(f"http://localhost:5003?level={level}")
    else:
        return redirect(url_for('gamepicker'))
    
@app.route('/play/<game>')
def play(game):
    level = request.args.get('level')
    if game == 'currency_roulette_game':
        return redirect(f"http://localhost:5001?level={level}")
    elif game == 'guess_game':
        return redirect(f"http://localhost:5002?level={level}")
    elif game == 'memory_game':
        return redirect(f"http://localhost:5003?level={level}")
    else:
        return redirect(url_for('gamepicker'))

@app.route('/savegame', methods=['POST'])
def savegame():
    add_score()
    return "Game result saved!"


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
        app.run(host="0.0.0.0", port=int(8777) ,debug=True)
    else:
        app.run(page_not_found)
