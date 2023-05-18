import streamlit as st

st.title("Diabetes prediction")
st.header("JONNALAGADDA SAIKUMAR")
st.header("lets CONNECT:")
st.write("LINKDIN: [link](https://www.linkedin.com/in/saikumar-jonnalagadda-305003215)")
st.write("GITHUB: [link](https://github.com/SaikumarJonnalagadda)")
    
    

btn_click1 = st.button("ABOUT THIS APP!")


if btn_click1 == True:
    st.write("""The Diabetes prediction dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. This dataset can be used to build machine learning models to predict diabetes in patients based on their medical history and demographic information. This can be useful for healthcare professionals in identifying patients who may be at risk of developing diabetes and in developing personalized treatment plans. Additionally, the dataset can be used by
              researchers to explore the relationships between various medical and demographic factors and the likelihood of developing diabetes.""")