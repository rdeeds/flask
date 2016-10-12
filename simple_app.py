from flask import (Flask, request, render_template,
                   redirect, url_for, make_response,
                   flash)
import json

app = Flask(__name__)
app.secret_key='y7182e7wyad8tfds67at32^T#dweas6gda1qdwqg1'

from options import DEFAULTS

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    data = get_saved_data()
    return render_template('index.html', saves=get_saved_data())

@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
    saves=get_saved_data(),options=DEFAULTS)


@app.route('/save', methods=['POST'])
def save():
    flash("fuck you and your Bear")
    response = make_response(redirect(url_for('builder')))
    #import pdb; pdb.set_trace()
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response


app.run(debug=True, port=8000, host='0.0.0.0')
