from flask import Flask, render_template, request, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from boggle import Boggle

boggle_game = Boggle()



app = Flask(__name__)
app.config['SECRET_KEY'] = 'dominos'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/')
def home_page():
    """shows home page"""

    board = boggle_game.make_board()
    # session['board'] = board

    return render_template("main.html", board=board)
