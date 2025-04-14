
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/wheater', methods=['GET'])
def clima():
  url = 'http://api.weatherapi.com/v1/current.json?key=2375a5443d77400e93e131230251404&q=London&aqi=no'

  response = requests.get(url)
  data = response.json()

  wheater_info = {
    'temperature': data['main']['temp'],
    'description': data['current']['condition']['text']
  }

  return jsonify(wheater_info)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
