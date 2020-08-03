from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)


@app.route('/')
def my_portfolio():
    print(url_for('static', filename='favicon.ico'))
    return render_template('./index.html')


@app.route('/index.html')
def my_home():
    return render_template('./index.html')


@app.route('/works.html')
def my_works():
    return render_template('works.html')


@app.route('/about.html')
def about_me():
    return render_template('about.html')


@app.route('/contact.html')
def my_contact():
    return render_template('contact.html')


@app.route('/components.html')
def my_components():
    return render_template('components.html')
