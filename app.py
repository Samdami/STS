from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {"admi2408eh8h3b": "password123", "use429776e87dhr": "usr3r74erpass"}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/updates")
def updates():
    return render_template("updates.html")


@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        # If a user submits an order form, redirect to the payment
        return redirect(url_for("checkout"))
    return render_template("order.html")


@app.route("/plan")
def plan():
    return render_template("cart.html")


@app.route("/payment")
def payment():
    return render_template("payment.html")


@app.route("/checkout")
def checkout():
    btc_address = "13g1gSf24R2UCeTbZ3BQy4ru7RhVbcBTTX"  # Replace with your BTC address
    usd_amount = 500  # Replace with the USD amount dynamically if necessary
    btc_amount = usd_amount * 0.000015  # Use the updated BTC conversion rate
    btc_amount = f"{btc_amount:.8f}"  # Format the BTC amount to 8 decimal places

    return render_template(
        "checkout_btc.html",
        btc_address=btc_address,
        amount=btc_amount,
    )


@app.route("/log")
def log():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username in users and users[username] == password:
        return f"Welcome, {username}!"
    else:
        return "Invalid credentials, please try again with your given password."


if __name__ == "__main__":
    app.run(debug=True)
