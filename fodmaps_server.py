# to run
# > FLASK_APP=fodmaps_server.py flask run

from flask import Flask, request, render_template
from back_end import fodmaps

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    #return fodmaps.get_fodmap_ingredients(request.form['ingredients'])
    data = fodmaps.get_fodmap_ingredients(request.form['ingredients'])
    return render_template('result.html', data = data)
    

if __name__=='__main__':
    app.run(debug=True)