from flask import Flask, request, jsonify
import util

app  = Flask(__name__)

@app.route('/get_loccation_naam')
def get_loccation_naam():
    response = josonify({
        'locations': util.get_loccation_naam()
    })
    response.headers.add('Access-Control-Allow-origin','*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    BHK = int(request.form['BHK'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,BHK,bath)
    })

    response.headers.add('Access-Control-Allow-origin','*')

    return response
if __name__ == "__main__":
    print("Let's Go for server for @day9 project in Batwebs")
    app.run()