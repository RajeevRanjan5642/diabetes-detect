# -*- coding: utf-8 -*-
"""
Rajeev Ranjan

Diabetes-Predictive-System
"""

# import all libraries
import numpy as np
import pickle
import streamlit as st

# loading the saved model
diabetes_model = pickle.load(open('C:/Users/ragha/OneDrive/Desktop/diabetes-prediction/diabetes_model.sav','rb'))

# creating a function for prediction
def diabetes_prediction(input_data):
    
    input_data = [float(x) for x in input_data]
    prediction = diabetes_model.predict([input_data])
    
    if prediction[0] == 0:
        return 'Non Diabetic'
    else:
        return 'Diabetic'
    
def main():
    
    st.title('Diabetes Prediction Web App')
    
    # Getting input from the user
    Glucose = st.text_input('Glucose:')
    Insulin = st.text_input('Insulin level:')
    BMI = st.text_input('BMI value: ')
    Age = st.text_input('Age:')
    
    # Code for prediction
    diagnosis = ''
    if st.button('Predict'):
        user_input = [Glucose, Insulin, BMI, Age]
        diagnosis = diabetes_prediction(user_input)
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()
    
    
    
