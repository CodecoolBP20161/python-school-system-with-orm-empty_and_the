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
        columns = ["first_name", "last_name", "city", "email"]
        a = [request.form[element] for element in columns]
        city = City.select().where(City.name == a[2])
        applicant = Applicant(first_name=a[0], last_name=a[1], city=city, email=a[3])
        applicant.save()
        flash("Application succesfull!")
        return redirect(url_for('home'))

app.run(debug=True)
