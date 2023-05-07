from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')


@app.route("/module")
def module():
    return render_template('module.html')


@app.route("/gallery")
def gallery1():
    return render_template('gallery.html')


@app.route("/gallery/<string:type>")
def gallery2(type=None):
    return render_template('gallery.html', type=type)


@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
