from flask import Flask, jsonify, request
from api import parser
import os
from dotenv import load_dotenv

load_dotenv()


PORT = os.environ.get("PORT")

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/get_restaurants_by_city/", methods=["POST"])
def get_restaurants_by_city():
    city_name = request.get_json()["city_name"]
    data = parser.ScraperForRestaurants(city_name)
    parsing_result = data.get_content()

    return jsonify(parsing_result)



if __name__ == '__main__':
    app.run(port=PORT, host='0.0.0.0')