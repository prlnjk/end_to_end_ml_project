import streamlit as st
import pickle
import pandas as pd

st.title("Car price predictor")

#col1, col2= st.beta_columns(2)
pipe=pickle.load(open("LinearRegressionModel.pkl","rb"))

def predict_price(car_name, company, year, kms_driven, fuel_type):
    input_data = pd.DataFrame({
        'name': [car_name],
        'company': [company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })
    prediction = pipe.predict(input_data)
    return prediction[0]

# Streamlit app
st.title('Second Hand Car Price Predictor')

st.header('Enter the details of the car')

car_name = st.text_input('Name of the car')
company = st.text_input('Company of the car')
year = st.number_input('Year of manufacture')
kms_driven = st.number_input('Kilometers driven')
fuel_type = st.selectbox('Fuel type', ['Petrol', 'Diesel', 'CNG', 'Electric', 'LPG'])

if st.button('Predict Price'):
    price = predict_price(car_name, company, year, kms_driven, fuel_type)
    st.write(f'The predicted price of the car is: ₹{price:.2f}')