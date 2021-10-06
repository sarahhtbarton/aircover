"""Server for Aircover Challenge."""

from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/print-ac', methods=['GET'])
def get_size():

    size = int(request.args.get('input-size')) #does request.args always return a string?
    a_thickness = 'A' * math.ceil(size/4)
    top_indentation = ' ' * (size + math.floor((size-1)/8) - 1)

    ac_list = []

    for i in range(size):
        if i == 0: #top row
            ac_list.append(top_indentation + a_thickness)
        elif i == math.floor(size/2): #middle row
            ac_list.append((' ' * (size - i - 1)) + a_thickness + ('A'*((i-1)*2)) + a_thickness)
        else: #all other rows
            ac_list.append((' ' * (size - i - 1)) + a_thickness + (' '*((i-1)*2)) + a_thickness)

    return render_template('print-ac.html',
                           ac_list=ac_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 