from flask import Flask, render_template, request, redirect, url_for, g, session
from flask.cli import load_dotenv
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object('config.Config')
app.config.from_prefixed_env()
babel = Babel(app)

load_dotenv()

@app.route('/')
def index():
    if 'lang' in session:
        session.pop('lang')
    return redirect(url_for('ddlanding', lang=get_locale()))


@app.route('/<string:lang>')
def ddlanding(lang=None):
    if lang and lang in app.config['LANGUAGES']:
        session['lang'] = lang
    g.locale = get_locale()
    return render_template('ddlanding.html')


@babel.localeselector
def get_locale():
    if 'lang' in session:
        return session['lang']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
