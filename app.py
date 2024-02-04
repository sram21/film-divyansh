from flask import Flask
from divyanshfilm.film import div_film

app = Flask(__name__, template_folder='/templates',static_url_path='/static')

app.register_blueprint(div_film)
