from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    total_per_person = None
    if request.method == "POST":
        try:
            rent = int(request.form["rent"])
            food = int(request.form["food"])
            electricity_bill = int(request.form["electricity"])
            water_bill = int(request.form["water"])
            gas_bill = int(request.form["gas"])
            person = int(request.form["person"])

            total = rent + food + electricity_bill + water_bill + gas_bill
            total_per_person = round(total / person, 2)
        except:
            total_per_person = "Invalid input. Please enter all values correctly."

    return render_template("index.html", result=total_per_person)

if __name__ == "__main__":
    app.run(debug=True)
