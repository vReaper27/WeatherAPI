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

        # Monta a resposta
        response_data = {'city': weather_data['city']}

        if fields:
            requested = [field.strip() for field in fields.split(',')]
            for field in requested:
                if field in weather_data:
                    response_data[field] = weather_data[field]
        else:
            # Se nenhum campo for especificado, retorna todos (menos o 'city' que já foi incluído)
            for key, value in weather_data.items():
                if key != 'city':
                    response_data[key] = value

        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
