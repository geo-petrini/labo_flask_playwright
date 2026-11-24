from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from modules.data_handler import write_data, read_data

app = Blueprint('default', __name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/data")
def data_page():
    data = read_data()
    return render_template('data.html', data=data)
    
@app.route("/data", methods=['POST'])
def data_submit():
    data = {
        'name' : request.form.get('name', '').strip(),
        'message' :request.form.get('message', '').strip()
    }
    write_data(data)
    return redirect( url_for('default.data_page') )