
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def weather():
    url = 'http://api.weatherapi.com/v1/current.json?key=2375a5443d77400e93e131230251404&q=London&aqi=no'

    response = requests.get(url)
    data = response.json()

    weather_info = {
        'temperature': data['current']['temp_c'],
        'description': data['current']['condition']['text']
    }

    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
