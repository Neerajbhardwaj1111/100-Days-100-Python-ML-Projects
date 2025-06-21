from flask import Flask, render_template, request
import requests

app =Flask(__name__)

API_URL = "https://api.frankfurter.app/latest"

@app.route("/",methods=["GET","POST"])
def index():
    result=None
    if request.method=="POST":
        amount=float(request.form["amount"])
        from_currency=request.form["from_currency"]
        to_currency=request.form["to_currency"]

        if from_currency == to_currency:
            result=amount
        else:
            response = requests.get(f"{API_URL}?amount={amount}&from={from_currency}&to={to_currency}")
            data = response.json()
            result = data["rates"][to_currency]
    
    currencies = ["USD", "EUR", "INR", "GBP", "JPY", "AUD", "CAD", "CHF"]
    return render_template("index.html", result=result, currencies=currencies)

if __name__ == "__main__":
    app.run(debug=False)

