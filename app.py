
import pickle
import pandas as pd
import numpy as np
import sklearn
import xgboost
from flask import Flask,request,render_template

app=Flask(__name__)

model = open("C:/users/daniel/documents/ds/car_price/carmodel.pkl","rb")
prediction=pickle.load(model)

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/predict",methods=["GET","POST"])

#Present_Price', 'Kms_Driven', 'Owner', 'Car_age',
#'Fuel_Type_Diesel', 'Fuel_Type_Petrol', 'Seller_Type_Individual',
#       'Transmission_Manual'

def predict():
    
    if request.method=="POST":
        Present_Price=int(request.form["Present_Price"])
       
        Kms_Driven=float(request.form["Kms_Driven"])
       
        Owner=int(request.form["Owner"])
       
        Car_age=int(request.form["Car_age"])
       
        Fuel_Type=(request.form["Fuel_Type"])
        
        if (Fuel_Type=="Diesel"):
            CNG=0
            Diesel=1
            Petrol=0
       
        elif (Fuel_Type=="Petrol"):
            CNG=0
            Diesel=0
            Petrol=1
       
        else:
            CNG=0
            Diesel=0
            Petrol=0          
    
        Seller_Type=request.form["Seller_Type"]
        if (Seller_Type == "Individual"):
            Individual=1
            Dealer=0
    
        else:
            Individual=0
            Dealer=1
           
        Transmission=request.form["Transmission"]
        if (Transmission=="Manual"):
            Manual=1
            Automatic=0
    
        else:
            Manual=0
            Automatic=1
       
        output=prediction.predict([[
            Present_Price,
            Kms_Driven,
            Owner,
            Diesel,
            Petrol,
            Individual,
            Manual,
            Car_age]])  
            
        output=round(output[0],2)
       
        return render_template("home.html", prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)