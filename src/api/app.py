from flask import Flask
from routes.sensor_routes import sensor_routes

app = Flask(__name__)

app.register_blueprint(sensor_routes, url_prefix="/api")

@app.route("/")
def home():
    return "¡Hola, bienvenido a la casa Mestaru!"

if __name__ == "__main__":
    app.run(debug=True)