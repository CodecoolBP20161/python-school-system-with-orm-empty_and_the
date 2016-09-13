from flask import *
from model_applicant import *
from model_city import *

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='development key'))


@app.route('/', methods=['GET'])
def root():
    return redirect(url_for('home'))


@app.route('/home', methods=['GET'])
def home():
    if request.method == "GET":
        return render_template("root.html")


@app.route('/applicant/login', methods=['GET'])
def login():
    if request.method == "GET":
        return "login page under construction"


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    city_list = City.select()
    if request.method == 'GET':
        return render_template("registration.html", city_list=city_list, form_data=request.form)
    elif request.method == 'POST':
        form_dict = dict((element, request.form[element]) for element in request.form)
        Applicant.create(**form_dict)
        flash("Application succesfull!")
        return redirect(url_for('home'))

app.run(debug=True)
