import os
import requests
from flask import Flask, request, render_template, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["SECRET_KEY"] = 'hushhhhhhh'
socketio = SocketIO(app)

votes = {"yes": 0, "no": 0, "maybe": 0}
@app.route('/')
def index():
    return render_template('index.html',votes=votes)


@socketio.on('submit vote')
def vote(data):
    selection = data["selection"]
    votes[selection] += 1
    emit("vote totals",votes,broadcast = True)