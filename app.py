import numpy as np
import pandas as pd
import datetime as dt
import os
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')
fet = pd.read_csv('all_features.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    features = [x for x in request.form.values()]

    # features[0] = Store, features[1] = Dept, features[2] = Date, features[3] = IsHoliday

    is_holiday_raw = features[3]
    is_holiday_bool = False if is_holiday_raw == '0' else True

    df = fet[
        (fet['Store'] == int(features[0])) &
        (fet['IsHoliday'] == is_holiday_bool) &
        (fet['Date'] == features[2])
        ].reset_index(drop=True)

    if df.shape[0] == 0:
        return render_template('index.html', output="No matching data found for the given inputs.")

    d = dt.datetime.strptime(features[2], '%Y-%m-%d')

    # IsHoliday_True: 1 if holiday, else 0
    is_holiday_encoded = 1 if is_holiday_bool else 0

    # The model was trained on exactly these 11 features in this order:
    # ['CPI', 'Day', 'Dept', 'Fuel_Price', 'IsHoliday_True', 'Month', 'Size', 'Store', 'Temperature', 'Unemployment', 'Year']
    f_features = [
        df['CPI'].iloc[0],  # CPI
        d.date().day,  # Day
        int(features[1]),  # Dept
        df['Fuel_Price'].iloc[0],  # Fuel_Price
        is_holiday_encoded,  # IsHoliday_True
        d.date().month,  # Month
        df['Size'].iloc[0],  # Size
        int(features[0]),  # Store
        df['Temperature'].iloc[0],  # Temperature
        df['Unemployment'].iloc[0],  # Unemployment
        d.date().year  # Year
    ]


    final_features = [np.array(f_features)]
    output = model.predict(final_features)[0]
    return render_template('index.html', output=output)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
