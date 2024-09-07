from flask import Flask, request
from guess_game import play
app = Flask(__name__)

@app.route('/')
def guess_game():
    level = request.args.get('level')
    play(level)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)