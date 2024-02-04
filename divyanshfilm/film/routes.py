from flask import render_template, request
from . import div_film


@div_film.route('/', methods=['GET','POST'])
def home():
    return render_template("home.html")


@div_film.route('/films', methods=['GET','POST'])
def films():
    return render_template("films.html", active_menu='films')


@div_film.route('/contact', methods=['GET','POST'])
def contact():
    return render_template("contact.html", active_menu='contact')