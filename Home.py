
import os
import flask
import jinja2


app = flask.Flask(__name__)
env = jinja2.Environment(
    loader=jinja2.PackageLoader(__name__,
                                'templates'))
app.secret_key = 'DontCryForMeArgentina!@#$%^'


@app.route('/')
def hello_world():
    template = env.get_template('base.html')
    html = template.render(ADDR=flask.request.environ['REMOTE_ADDR'],
                           CLIENT=flask.request.environ['HTTP_USER_AGENT'])
    return html


if __name__ == '__main__':
    """
    Application entry point
    """
    use_debugger = False
    app.run()