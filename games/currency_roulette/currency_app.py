from flask import Flask, request
from currency_roulette_game import play
app = Flask(__name__)

@app.route('/')
def currency_roulette_game():
    level = request.args.get('level')
    play(level)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)