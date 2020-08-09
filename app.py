"""
Streamlit is being used to productionize the model

"""
import numpy as np
import pickle
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import streamlit as st

# Load the Catboost Classifier model / Random Forest is also good
filename = 'ctb_hepatitis.pkl'
classifier = pickle.load(open(filename, 'rb'))

def main():

    html_temp = """
        <div style="background-color:orange">
            <p style="color:white; font-size:55px"> Hepatitis Survival Prediction</p>
            <p style="color:white; font-size:13px"> Developer : Prakash Dahal</p>
        </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    st.title("Check whether you will survive or not, of hepatitis")

    #Getting values from the users
    protime = st.number_input("Enter Protime value (eg: 45)", value= 45,min_value=0)

    sgot = st.number_input("Enter Sgot value (eg: 30)", value=30, min_value=0)

    bilirubin = float(st.number_input("Enter Bilirubin value (eg: 1.2)",value=1.2, min_value=0.0))

    age = st.number_input("Enter your Age value (eg: 35)",value=35, min_value=1, max_value=150)

    alk_phosphate = st.number_input("Enter Alkaline phosphate value (eg: 90)", value=90, min_value=0)

    albumin = float(st.number_input("Enter Albumin value (eg: 4.1)", value=4.1, min_value=0.0))

    spiders = st.number_input("Enter Spider value (eg: 1 or 2)", value=1, min_value=1,max_value=2)

    histology = st.number_input("Enter Histology value (eg: 1 or 2)",value=1, min_value=1,max_value=2)

    malaise= st.number_input("Enter Malaise value (eg: 1 or 2)",value=1, min_value=1,max_value=2)

    fatigue= st.number_input("Enter Fatigue value (eg: 1 or 2)",value=1, min_value=1,max_value=2)

    sex= st.number_input("Enter sex value (eg: 1 for male, 2 for female)",value=1, min_value=1,max_value=2)


    values = [[protime, sgot, bilirubin, age, alk_phosphate, albumin, spiders, histology,
              malaise, fatigue, sex]]

    #val = [[0.0, 114.0, 1.9, 45.0, 0.0, 2.4, 1.0, 2.0, 1.0, 1.0, 1.0]]

    new_values = np.array(values)
    prediction = classifier.predict(new_values)
    percent = (classifier.predict_proba(new_values)[0][1]) * 100
    percent = round(percent,2)
    percent = f"{percent} % chance"
    print(percent)
    btn = st.button("Predict")
    if btn:
        if prediction == [0]: # 0 is for not surviving
            html_temp1 = """
                        <div style="background-color:red">
                            <p style="color:white; font-size:35px"> Sorry, your chance of survival is less</p>
                        </div>
                    """
            st.text(percent)
            st.markdown(html_temp1, unsafe_allow_html=True)
            with open("sad.jpg", 'rb') as f:
                img = f.read()
            st.image(img, width=350)

        if prediction == [1]:  # 1 is for surviving
            html_temp1 = """
                                <div style="background-color:green">
                                    <p style="color:white; font-size:35px"> Hurray!!!, your chance of survival is high</p>
                                </div>
                            """
            st.text(percent)
            st.markdown(html_temp1, unsafe_allow_html=True)
            with open("happy.jpg", 'rb') as f:
                imgg = f.read()
            st.image(imgg, width=350)


if __name__ == '__main__':
    main()