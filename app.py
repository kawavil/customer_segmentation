from flask import Flask, request, render_template
import pickle
import stockinfo_retrive as sr

app = Flask(__name__, static_url_path='/static')

pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)

index_vals = {}


@app.route('/', methods=['GET'])
def index():
    global index_vals
    index_vals = sr.get_quotes()
    return render_template('home.html', info=index_vals)


@app.route('/predict', methods=["POST"])
def predict():
    age = request.form['age']
    savings = request.form['savings']
    food = request.form['food']
    gadget = request.form['gadget']
    clothing = request.form['clothing']
    allexp = {'Food': int(food), 'Gadget': int(gadget), 'Clothing': int(clothing)}
    maxexp = max(allexp, key=allexp.get)
    print("Max Expense ", maxexp)
    # print("Max value of that key ", allexp.get(maxexp))
    age, savings = int(age), int(savings)
    result = model.predict([[age, savings]])
    pred = ''
    if age < int(18):
        pred = "Please sit back and relax for few years"
    else:
        if result[0] == 0:
            if 18 <= age <= 28:
                if savings >= 600:
                    pred = "You can invest in options and derivatives"
                else:
                    pred = "You can invest in equitis and gold"
            elif 28 < age <= 35:
                if savings >= 700:
                    pred = "You can invest in equities with strict stoploss"
                else:
                    pred = "You can invest in index funds and mutual funds"
            elif 35 < age <= 50:
                if savings >= 400:
                    pred = "You can invest in mutual funds"
                else:
                    pred = "You can invest in fixed deposits and bonds"
            elif age > 50:
                if savings >= 300:
                    pred = "You can invest in fixed deposits"
                else:
                    pred = "You can invest in Term Insurance"

        elif result[0] == 1:
            if 18 <= age <= 28:
                if savings >= 600:
                    pred = "You can invest in options and derivatives"
                else:
                    pred = "You can invest in equitis and gold"
            elif 28 < age <= 35:
                if savings >= 700:
                    pred = "You can invest in equities with strict stoploss"
                else:
                    pred = "You can invest in index funds and mutual funds"
            elif 35 < age <= 50:
                if savings >= 400:
                    pred = "You can invest in mutual funds"
                else:
                    pred = "You can invest in fixed deposits and bonds"
            elif age > 50:
                if savings >= 300:
                    pred = "You can invest in fixed deposits"
                else:
                    pred = "You can invest in Term Insurance"

        elif result[0] == 2:
            if 18 <= age <= 28:
                if savings >= 600:
                    pred = "You can invest in options and derivatives"
                else:
                    pred = "You can invest in equitis and gold"
            elif 28 < age <= 35:
                if savings >= 700:
                    pred = "You can invest in equities with strict stoploss"
                else:
                    pred = "You can invest in index funds and mutual funds"
            elif 35 < age <= 50:
                if savings >= 400:
                    pred = "You can invest in mutual funds"
                else:
                    pred = "You can invest in fixed deposits and bonds"
            elif age > 50:
                if savings >= 300:
                    pred = "You can invest in fixed deposits"
                else:
                    pred = "You can invest in Term Insurance"

        elif result[0] == 3:
            if 18 <= age <= 28:
                if savings >= 600:
                    pred = "You can invest in options and derivatives"
                else:
                    pred = "You can invest in equitis and gold"
            elif 28 < age <= 35:
                if savings >= 700:
                    pred = "You can invest in equities with strict stoploss"
                else:
                    pred = "You can invest in index funds and mutual funds"
            elif 35 < age <= 50:
                if savings >= 400:
                    pred = "You can invest in mutual funds"
                else:
                    pred = "You can invest in fixed deposits and bonds"
            elif age > 50:
                if savings >= 300:
                    pred = "You can invest in fixed deposits"
                else:
                    pred = "You can invest in Term Insurance"

        elif result[0] == 4:
            if 18 <= age <= 28:
                if savings >= 600:
                    pred = "You can invest in options and derivatives"
                else:
                    pred = "You can invest in equitis and gold"
            elif 28 < age <= 35:
                if savings >= 700:
                    pred = "You can invest in equities with strict stoploss"
                else:
                    pred = "You can invest in index funds and mutual funds"
            elif 35 < age <= 50:
                if savings >= 400:
                    pred = "You can invest in mutual funds"
                else:
                    pred = "You can invest in fixed deposits and bonds"
            elif age > 50:
                if savings >= 300:
                    pred = "You can invest in fixed deposits"
                else:
                    pred = "You can invest in Term Insurance"

        else:
            pred = 'some error'
    print("Cluster ", result[0])
    # param = {'result': pred, 'info':params}
    return render_template('home.html', result=pred, info=index_vals, exp=maxexp)


if __name__ == '__main__':
    app.run(debug=True)
