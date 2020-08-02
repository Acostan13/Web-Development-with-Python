from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    print(url_for('static', filename='favicon.ico'))
    return render_template('./index.html')


@app.route('/<username>')
def user_name(username=None):
    return render_template('./index.html', name=username)


@app.route('/<username>/<int:post_id>')
def user_name_and_post_id(username=None, post_id=None):
    return render_template('./index.html', name=username, post_id=post_id)


@app.route('/about.html')
def about():
    return render_template('./about.html')


@app.route('/blog')
def blog():
    return 'These are my thoughts on blogs.'


@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my dog'
