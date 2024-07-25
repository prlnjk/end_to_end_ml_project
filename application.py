from flask import Flask
import pandas as pd
app=Flask(__name__)
car=pd.read_csv("cleaned_car_csv.csv")
@app.route('/')
def index():
    return "Hello"

if __name__=="__main__":
    app.run(debug=True)