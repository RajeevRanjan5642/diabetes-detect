# -*- coding: utf-8 -*-
"""
Author : Rajeev Ranjan

Diabetes-Predictive-System
"""

# import all libraries
import pickle
import streamlit as st

# loading the saved model
diabetes_model = pickle.load(open('./model/diabetes_model.pkl','rb'))

# creating a function for prediction
def diabetes_prediction(input_data):
    
    input_data = [float(x) for x in input_data]
    prediction = diabetes_model.predict([input_data])
    
    if prediction[0] == 0:
        return 'Non Diabetic'
    else:
        return 'Diabetic'
    
def main():
    
    st.title('Diabetes-Detect')
    
    # Getting input from the user
    Pregnancies = st.text_input('Pregnancies:')
    Glucose = st.text_input('Glucose:')
    BloodPressure = st.text_input('BloodPressure:')
    SkinThickness = st.text_input('SkinThickness:')
    Insulin = st.text_input('Insulin level:')
    BMI = st.text_input('BMI value: ')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction:')
    Age = st.text_input('Age:')
    
    # Code for prediction
    diagnosis = ''
    if st.button('Predict'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diagnosis = diabetes_prediction(user_input)
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()
    
    
    
