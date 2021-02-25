from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=["POST"])
def predict():
    inputs = [val for val in request.form.values()]
    result = model.predict([[inputs[0], inputs[1]]])
    pred = ''
    if result[0] == 0:
        pred = "You can invest in Equity market for long and short term as well as in bonds"
    elif result[0] == 1:
        pred = "You can invest in Equity market for long and short term"
    elif result[0] == 2:
        pred = "You can invest in Equity market, bonds and start intraday with strict stoploss"
    elif result[0] == 3:
        pred = "You can invest in Equity market, bonds and also trade in intraday"
    elif result[0] == 4:
        pred = "You can invest in Equity market for long term"
    else:
        pred = 'some error'
    return render_template('index.html', result=pred)


if __name__ == '__main__':
    app.run(debug=True)
