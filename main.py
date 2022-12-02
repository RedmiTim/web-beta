import flask


app = flask.Flask(__name__)


def index():
    return '<h1>hello world</h1>'


def another_page():
    a = flask.request.args['a']
    b = flask.request.args['b']
    return 'Вы передали: ' + a + ' и ' + b


app.add_url_rule('/', view_func=index)
app.add_url_rule('/another', view_func=another_page)
app.run(debug=True)
