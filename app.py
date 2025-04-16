from flask import Flask
from routes import weather_bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.register_blueprint(weather_bp)
