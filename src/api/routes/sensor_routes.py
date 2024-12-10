from flask import Blueprint, request, jsonify

sensor_routes = Blueprint("sensor_routes", __name__)

@sensor_routes.route("/data",methods=["POST"])
def receive_data():
    data = request.get_json()
    if not data:
        return jsonify({"error":"No data provided"}), 400
    
    print(f"Datos recibidos: {data}")

    return jsonify({"message":"Datos recibidos correctamente"}), 200