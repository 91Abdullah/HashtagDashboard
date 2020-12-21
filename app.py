from flask import Flask, jsonify, request
from flask import render_template
import ast
app = Flask(__name__)
labels = []
values = []
sentiments = []
frequency = []


@app.route('/')
def get_chart_page():
    global labels, values
    labels = []
    values = []
    return render_template('chart.html', values=values, labels=labels)


@app.route('/refreshData')
def refresh_graph_data():
    global labels, values
    print("labels are now: " + str(labels))
    print("data is now: " + str(values))
    return jsonify(sLabel=labels, sData=values)


@app.route('/updateData', methods=['POST'])
def update_data():
    global labels, values
    if not request.form or 'data' not in request.form:
        return "error", 400
    labels = ast.literal_eval(request.form['label'])
    values = ast.literal_eval(request.form['data'])
    print("labels received: " + str(labels))
    print("data received: " + str(values))
    return "success", 201


@app.route('/refreshSentiments')
def refresh_sentiments():
    global sentiments, frequency
    print("labels for sentiments are: " + str(sentiments))
    print("data for sentiments is: " + str(frequency))
    return jsonify(sSentiments=sentiments, aData=frequency)


@app.route('/updateSentiments', methods=['POST'])
def update_sentiments():
    global sentiments, frequency
    if not request.form or 'data' not in request.form:
        return 'error', 400
    sentiments = ast.literal_eval(request.form['label'])
    frequency = ast.literal_eval(request.form['data'])
    print('Sentiments data received: ' + str(frequency))
    print('Sentiments labels received: ' + str(sentiments))
    return "success", 201


if __name__ == '__main__':
    app.run(host='localhost', port=5001)
