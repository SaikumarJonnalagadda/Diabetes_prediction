import streamlit as st
import numpy as np
from pickle import load
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler


scaler = load(open('models/standard_scaler.pkl', 'rb'))
sv_model = load(open('models/sv_model.pkl', 'rb'))


a = st.text_input("Pregnancies", placeholder="Enter no of Pregnancies ")
b = st.text_input("Glucose level", placeholder="Enter value in mg/dL")
c = st.text_input("BloodPressure", placeholder="Enter value ")
d = st.text_input("SkinThickness", placeholder="Enter value in mm")
e = st.text_input("Insulin", placeholder="Enter value in mcU/mL")
f = st.text_input("Body mass index(BMI)", placeholder="Enter value in KG")
g = st.text_input("DiabetesPedigreeFunction", placeholder="Enter value ")
h = st.text_input("Age", placeholder="Enter Age")



btn_click = st.button("Predict")

if btn_click == True:
    if a and b and c and d and e and f and g and h:
        query_point = np.array([int(a), int(b),int(c),int(d),int(e), float(f), float(g),int(h)]).reshape(1, -1)
        query_point_transformed = scaler.transform(query_point)
        pred = sv_model.predict(query_point_transformed)
        if pred==0:
            st.success("Not presence of diabities")
        else:
            st.success("presence of diabities")