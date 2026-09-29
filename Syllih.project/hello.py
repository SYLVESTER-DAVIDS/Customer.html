from flask import Flask, render_template, request

app = Flask(__name__)

# ATM information
CORRECT_PIN = "1234"
balance = 5000


@app.route("/")
def home():
    return render_template("index.html", logged_in=False)


@app.route("/login", methods=["POST"])
def login():
    pin = request.form["pin"]

    if pin == CORRECT_PIN:
        return render_template(
            "index.html",
            logged_in=True,
            balance=balance,
            message="Login successful!"
        )
    else:
        return render_template(
            "index.html",
            logged_in=False,
            message="Incorrect PIN!"
        )


if __name__ == "__main__":
    app.run(debug=True)