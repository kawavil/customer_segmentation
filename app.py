from flask import Flask, request, render_template
import pickle
import stockinfo_retrive as sr

app = Flask(__name__, static_url_path='/static')

pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)


@app.route('/', methods=['GET'])
def index():
    params = sr.get_quotes()
    # params = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
    return render_template('home.html', info=params)


@app.route('/predict', methods=["POST"])
def predict():
    inputs = [val for val in request.form.values()]
    print(inputs)
    result = model.predict([[inputs[0], inputs[1]]])
    pred = ''
    savings = 0
    # savings = (int(inputs[2])/100)*int(inputs[1])
    age = int(inputs[0])
    if int(inputs[0]) < int(18):
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
    return render_template('index.html', result=pred)


if __name__ == '__main__':
    app.run(debug=True)
