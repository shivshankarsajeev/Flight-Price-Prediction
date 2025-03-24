from flask import Flask, render_template
from flask_cors import cross_origin
import pickle 
import sklearn 
import pandas as pd 


app = Flask(__name__)
model = pickle.load(open('flight_rf.pkl','rb'))

@app.route("/")
@cross_origin()
def home(): 
    return render_template("home.html")

@app.route("/predict", methods = ["GET","POST"])
@cross_origin
def predict(): 
    if request.method == "POST":

        ## Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format = "%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format = "%Y-%m-%dT%H:%M").month)
        #print(Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format = "%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format = "%Y-%m-%dT%H:%M").minute)
        #print(Dep_hour, Dep_min)

        output = 50
        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("home.html")






if __name__=="__main__": 
    app.run(debug=True)
