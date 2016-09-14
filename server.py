from flask import *
from model_applicant import *
from model_city import *
from model_interview_slot import *

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='development key'))


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET'])
def root():
    if request.method == "GET":
        return redirect(url_for('home'))


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("root.html")
    if request.method == "POST":
        querry = Applicant.select().where(Applicant.email == request.form["email"])
        if querry:
            applicant = querry.get()
            if str(applicant.application_code) == request.form["code"]:
                return render_template("root.html", applicant=applicant)
            else:
                flash("Invalid Application code! Please try again!")
                return render_template("root.html", warning="code")
        else:
            flash("This e-mail address is not registered!")
            return render_template("root.html", warning="email")


@app.route('/forget', methods=['GET', 'POST'])
def forget():
    if request.method == "GET":
        return render_template("forget.html")
    if request.method == "POST":
        querry = Applicant.select().where(Applicant.email == request.form["email"])
        if querry:
            applicant = querry.get()
            applicant.send_code_reminder()
            flash("E-mail reminder about application has been sent!")
            return redirect(url_for('home'))
        else:
            flash("This e-mail address is not registered!")
            return render_template("forget.html", warning="email")


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    city_list = City.select()
    if request.method == 'GET':
        return render_template("registration.html", city_list=city_list)
    elif request.method == 'POST':
        for element in Applicant.select(Applicant.email):
            if request.form['email'] == element.email:
                flash("The e-mail address you specified is already in use.")
                return redirect(url_for('registration'))
        form_dict = dict((element, request.form[element]) for element in request.form)
        applicant = Applicant.create(**form_dict)
        applicant.get_school()
        applicant.code_generator()
        InterviewSlot.get_interview_for_applicant(applicant)
        flash("Application succesfull!")
        return redirect(url_for('home'))

app.run(debug=True)
