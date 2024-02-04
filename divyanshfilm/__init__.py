from flask import Flask


def create_app():
    app = Flask(__name__, static_url_path='/static')
    from divyanshfilm.film import div_film
    app.register_blueprint(div_film)

    return app