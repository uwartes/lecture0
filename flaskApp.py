# Flask web app 
# use Flask module, render template to use html templates
# request is needed for method post
# session to store session variables
# pip install Flask-Session
from flask import Flask, render_template, request, session
from flask_session import Session
import datetime

#add sqlalchemy
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


# __name__ means this current file will be the flask app 
app = Flask(__name__)

# config to store session variables
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#connect to database
engine = create_engine("postgresql://postgres:tajuana@localhost/myDB")
db = scoped_session(sessionmaker(bind=engine))


# the function immediately below the @app.route() will be run 
@app.route("/")
def index():
    return "<h1>Hello Flask App</h1> goto /about for more info"

@app.route("/flights")
def flights():
    flights = db.execute("select * from flights").fetchall()
    return render_template("flights.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""
    #get from information
    name = request.form.get("name")
   
    #check id is integer
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid Flight Number")
   
    #make sure the flight exists
    if db.execute("select * from flights where id = :id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flitht with that id")
    
    db.execute("insert into passengers (name, flight_id) values(:name, :flight_id)",
            {"name":name, "flight_id": flight_id})
    db.commit()
    return render_template("error.html", message="Passenger succesfully added to flight")

@app.route("/flightDetail/<int:flight_id>")
def flightDetail(flight_id):
    #Get flight info
    flight = db.execute("select * from flights where id = :id", {"id": flight_id}).fetchone()
    if flight is None:
        return render_template("error.html", message="No such flight")

    passengers = db.execute("select name from passengers where flight_id = :flight_id", 
                              {"flight_id":flight_id}).fetchall()

    return render_template("flightDetail.html", flight=flight, passengers=passengers)
       
   

@app.route("/tanzania")
def tanzania():
    return render_template("tanzania.html")

@app.route("/name/<string:name>")
def hello(name):
    name = name.capitalize()   # capitalize first letter
    return f"<h3>Hello people of {name}</h3>"

@app.route("/about")
def about():
    headline="We are about about it"
    now = datetime.datetime.now()
    newYear = now.month == 1 and now.day == 1   # if month=1 and day=1 (jan1) set boolean vnewYear True
    nameList = ["Alice", "Bob", "Harry"]
    return render_template("about.html",headline=headline, newYear=newYear, nameList=nameList)


# helloForm extends layout.html and has input form post method
# calls helloFormResp when submitted

@app.route("/helloForm")
def helloForm():
    return render_template("helloForm.html")

# get the name entered on helloForm and render helloFormResp
@app.route("/helloFormResp", methods=["GET","POST"])
def helloFormResp():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("helloFormResp.html", name=name)
    else:
        return render_template("helloForm.html") 


# global empty list of notes every one sees
# to make that only one person sees, use session in route
#notes = []   
@app.route("/notesApp", methods=["GET","POST"])
def notesApp():
    # init notes when empty, else add to it
    if session.get("notes") is None:
        session["notes"] = []

    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    
    return render_template("notes.html", notes=session["notes"])
   