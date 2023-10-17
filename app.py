from flask import Flask, render_template, request

app = Flask(__name__)  # turn this file into a flask application

SPORTS = ["Cricket", "Football", "Basketball", "Kabaddi"]


@app.route("/")
def index():
    # name = request.args.get("name")
    # return render_template("index.html", nameOfPerson=name)
    return render_template("index.html", sports=SPORTS)


# @app.route("/greet") # for get request
# def greet():
#     name = request.args.get("name", "world")  # default value is "world"
#     return render_template("greet.html", name=name)

@app.route("/register", methods=["POST"])
def register():
    # validate submission
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")

    # confirm registration
    return render_template("success.html")
