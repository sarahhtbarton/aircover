"""Server for Aircover Challenge."""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/print-ac', methods=['GET'])
def get_size():

    size = request.args.get('input-size') #this is a dictionary. Must be args (not form) in a GET request

    return render_template('print-ac.html',
                           size=size)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 