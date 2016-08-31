from flask import *
from model_applicant import *
from model_city import *

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='development key'))


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    city_list = ["Choose a city!", "Kaposvár", "Érd", "Visegrád", "Veszprém", "Sopron", "Kecskemét", "Győr", "Gödöllő",
                 " Hatvan", "Vác", "Eger", "Nyíregyháza", "Debrecen", "Kiskőrös", "Gyula", "Hajdúszoboszló", "Kassa",
                 "Wieliczka", "Liszki", "Katowice", "Varsó", "Berlin"]
    if request.method == 'GET':
        return render_template("registration.html", city_list=city_list, form_data=request.form)
    elif request.method == 'POST':
        columns = ["first_name", "last_name", "city", "email"]
        a = [request.form[element] for element in columns]
        if all(a) and request.form["city"] != "Choose":
            print(request.form["city"])
            c = City.select(City.id).where(City.name == a[2])
            applicant = Applicant(first_name=a[0], last_name=a[1], city=c, email=a[3])
            applicant.save()
            return redirect(url_for('succesfull'))
        else:
            flash("Please fill!")
            return render_template("registration.html", city_list=city_list, form_data=request.form)


@app.route('/registration/succesfull')
def succesfull():
    return render_template("succesfull.html")

app.run(debug=True)
