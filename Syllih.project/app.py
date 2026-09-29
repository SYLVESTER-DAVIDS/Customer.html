from flask import Flask, render_template, request, redirect, url_for

# Create Flask application
app = Flask(__name__)

# ATM information
CORRECT_PIN = "3333"
balance = 5000.00


# Home page
@app.route("/")
def home():
    return render_template(
        "index.html",
        logged_in=False,
        message=""
    )


# Login
@app.route("/login", methods=["POST"])
def login():
    global balance

    pin = request.form.get("pin")

    if pin == CORRECT_PIN:
        return render_template(
            "index.html",
            logged_in=True,
            balance=balance,
            message="Login successful!"
        )

    return render_template(
        "index.html",
        logged_in=False,
        message="Incorrect PIN. Please try again."
    )


# Deposit money
@app.route("/deposit", methods=["POST"])
def deposit():
    global balance

    amount = float(request.form.get("amount", 0))

    if amount <= 0:
        message = "Please enter a valid amount."
    else:
        balance += amount
        message = f"Deposit successful. Ksh {amount:,.2f} added."

    return render_template(
        "index.html",
        logged_in=True,
        balance=balance,
        message=message
    )


# Withdraw money
@app.route("/withdraw", methods=["POST"])
def withdraw():
    global balance

    amount = float(request.form.get("amount", 0))

    if amount <= 0:
        message = "Please enter a valid amount."

    elif amount > balance:
        message = "Insufficient balance."

    else:
        balance -= amount
        message = f"Withdrawal successful. Ksh {amount:,.2f} withdrawn."

    return render_template(
        "index.html",
        logged_in=True,
        balance=balance,
        message=message
    )


# Logout
@app.route("/logout")
def logout():
    return redirect(url_for("home"))


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)