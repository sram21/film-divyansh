from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route('/films', methods=['GET','POST'])
def films():
    return render_template("films.html", active_menu='films')

@app.route('/contact', methods=['GET','POST'])
def contact():
    return render_template("contact.html", active_menu='contact')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
