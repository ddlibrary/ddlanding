import datetime

from flask import Flask, render_template, request, redirect, url_for, g, session, make_response
from flask.cli import load_dotenv
from flask_babel import Babel

load_dotenv()

app = Flask(__name__)
app.config.from_object('config.Config')
app.config.from_prefixed_env()
babel = Babel(app)


@app.route('/')
def index():
    if 'lang' in session:
        session.pop('lang')
    return redirect(url_for('ddlanding', lang=get_locale()))


@app.route('/<path:lang>')
def ddlanding(lang=None):
    potential_query_string = ""
    if lang and lang in app.config['LANGUAGES']:
        session['lang'] = lang
    else:
        return redirect("https://library.darakhtdanesh.org/" + lang)
    g.locale = get_locale()
    if request.cookies.get('has_read_intro'):
        return render_template('ddlanding.html', potential_query_string=potential_query_string, intro_modal=False)
    else:
        response = make_response(render_template('ddlanding.html',
                                                 potential_query_string=potential_query_string,
                                                 intro_modal=True
                                                 )
                                 )
        now = datetime.datetime.now()
        expiry_date = now + datetime.timedelta(days=30)
        response.set_cookie('has_read_intro', 'yes', expires=expiry_date)
        return response


@app.route('/ddcourses/<string:lang>')
def ddcourses(lang=None):
    if lang and lang in app.config['LANGUAGES']:
        session['lang'] = lang
    g.locale = get_locale()
    return render_template('portal.html')


@app.route('/ddcourses/oruj/<string:lang>')
def oruj(lang=None):
    if lang and lang in app.config['LANGUAGES']:
        session['lang'] = lang
    g.locale = get_locale()
    return render_template('oruj.html')


@babel.localeselector
def get_locale():
    if 'lang' in session:
        return session['lang']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
