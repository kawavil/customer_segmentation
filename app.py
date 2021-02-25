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
        pred = "You belongs to cluster 1"
    elif result[0] == 1:
        pred = "You belongs to cluster 2"
    elif result[0] == 2:
        pred = "You belongs to cluster 3"
    elif result[0] == 3:
        pred = "You belongs to cluster 4"
    elif result[0] == 4:
        pred = "You belongs to cluster 5"
    else:
        pred = 'some error'
    return render_template('index.html', result=pred)


if __name__ == '__main__':
    app.run(debug=True)
