from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("home_page.html")


@app.route('/Connect4/', methods=["GET", "POST"])
def connect_4():
    return render_template("connect_4.html")

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=80)
    app.run()