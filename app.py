from flask import Flask
from divyanshfilm.film import div_film

app = Flask(__name__, template_folder='/divyanshfilm/templates',static_url_path='/divyanshfilm/static')

app.register_blueprint(div_film)
