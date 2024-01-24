from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

messages = []

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_messages(data):
    messages.append(data)
    emit("message", data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)
