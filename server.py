from flask import *
from model_applicant import *
from model_city import *


app = Flask(__name__)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        city_list = ["Kaposvár", "Érd", "Visegrád", "Veszprém", "Sopron", "Kecskemét", "Győr", "Gödöllő", " Hatvan",
                     "Vác", "Eger", "Nyíregyháza", "Debrecen", "Kiskőrös", "Gyula", "Hajdúszoboszló", "Kassa",
                     "Wieliczka", "Liszki", "Katowice", "Varsó", "Berlin"]
        return render_template("registration.html", city_list=city_list)
    elif request.method == 'POST':
        columns = ["first_name", "last_name", "city", "email"]
        a = [request.form[element] for element in columns]
        c = City.select(City.id).where(City.name == a[2])
        applicant = Applicant(first_name=a[0], last_name=a[1], city=c, email=a[3])
        applicant.save()
        return redirect(url_for('succesfull'))

@app.route('/registration/succesfull')
def succesfull():
    return render_template("succesfull.html")

app.run(debug=True)
