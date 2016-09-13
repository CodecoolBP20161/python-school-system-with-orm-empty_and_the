from flask import *
from model_applicant import *
from model_city import *
from model_user import *

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='development key'))


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    city_list = City.select()
    if request.method == 'GET':
        return render_template("registration.html", city_list=city_list, form_data=request.form)
    elif request.method == 'POST':
        columns = ["first_name", "last_name", "city", "email"]
        a = [request.form[element] for element in columns]
        if all(a) and request.form["city"] != "nocity":
            city = City.select().where(City.name == a[2])
            applicant = Applicant(first_name=a[0], last_name=a[1], city=city, email=a[3])
            applicant.save()
            return redirect(url_for('succesfull'))
        else:
            flash("Please do not leave unanswered question boxes or blanks!")
            return render_template("registration.html", city_list=city_list, form_data=request.form)


@app.route('/registration/succesfull')
def succesfull():
    return render_template("succesfull.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        if User.select().where(User.username == request.form["username"]):
            return redirect(url_for('admin', login=True))
        else:
            return render_template("login.html")
            flash("Invalid username or password!")


@app.route('/admin', methods=['GET'])
@app.route('/admin/<userid>', methods=['GET'])
def admin(userid='', login=False):
    if login:
        return render_template("succesfull.html")
    else:
        return redirect(url_for('login'))

app.run(debug=True)
