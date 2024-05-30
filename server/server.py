from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_sublocality_names')
def get_sublocality_names():
    response = jsonify({

    })

if __name__ == '__main__':
    print('Server is running...')
    app.run()