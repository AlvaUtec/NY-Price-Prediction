from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_sublocality_names')
def get_sublocality_names():
    response = jsonify({
        'sublocalities': util.get_sublocalities()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    print('Request received...')
    sublocality = request.form['sublocality']
    sqft = float(request.form['sqft'])
    bath = int(request.form['bath'])
    beds = int(request.form['beds'])

    ans = float(util.get_estimated_price(sublocality, sqft, bath, beds))

    response = jsonify({
        'estimated_price': ans
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    print('Server is running...')
    util.load_saved_artifacts()
    app.run()