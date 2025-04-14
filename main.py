
from flask import Flask, jsonify, request, redirect
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/weather')

@app.route('/weather', methods=['GET'])
def get_weather():
  
  API_KEY = os.getenv('API_KEY')
  city = request.args.get('city', default= None, type = str) 
  
  url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no'

  try:
        response = requests.get(url)
        data = response.json()

        weather_info = {
            'temperature': data['current']['temp_c'],
            'description': data['current']['condition']['text']
        }

        return jsonify(weather_info)
  except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
