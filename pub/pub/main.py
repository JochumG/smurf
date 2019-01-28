from flask import Flask
import uwsgi

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hey I'm using Docker! Az well"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
