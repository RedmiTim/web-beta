import flask
app=flask.Flask(__name__)
def index():
    return '<h1>hello world<h1>'
def another_page():
    return 'это вторая страница. <a href="/">на главную</a>'
app.add_url_rule('/',view_func=index)
app.add_url_rule('/another', view_func=another_page)
app.run(debug=True)
