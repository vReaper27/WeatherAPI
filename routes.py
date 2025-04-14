from flask import Blueprint, jsonify, request
from services import fetch_weather_data

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    fields = request.args.get('fields')

    if not city:
        return jsonify({'error': 'Cidade não especificada'}), 400

    try:
        weather_data = fetch_weather_data(city)

        # Extrai os campos pedidos, se houver
        selected_fields = {}
        if fields:
            requested = [field.strip() for field in fields.split(',')]
            for field in requested:
                if field in weather_data:
                    selected_fields[field] = weather_data[field]

        # Insere a cidade como primeiro item
        response_data = {'city': weather_data['city']}
        response_data.update(selected_fields)

        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
