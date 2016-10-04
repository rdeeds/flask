from flask import (Flask, request, render_template,
                   redirect, url_for, make_response)
import json

app = Flask(__name__)


def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
        dd = json.pa
    return data


@app.route('/')
def index():
    data = get_saved_data()
    return render_template('index.html', saves=data)


@app.route('/save', methods=['POST'])
def save():
    response = make_response(redirect((url_for('index'))))
    #   import pdb; pdb.set_trace()
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response


app.run(debug=True, port=8000, host='0.0.0.0')
