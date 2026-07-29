import pandas as pd
import streamlit as st
import pickle as pk

#Now we are loading the pickle file in model and scaler
model = pk.load(open("model.pkl","rb"));
scaler = pk.load(open("scaler.pkl","rb"));

st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="centered"
)
background_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #89CFF0;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(background_css, unsafe_allow_html=True)


st.title('🤖 Loan Approval Prediction')

no_of_dependt = st.slider(" Choose No. of Dependents",0,5)
education = st.selectbox("Choose Education",["Graduate","Not Graduate"])
self_emply = st.selectbox("Self Employed",["Yes","No"])
income_annum = st.slider("Choose Annual Income",0,10000000)
loan_ammount = st.slider("Choose Loan Amount",0,10000000)
loan_duration = st.slider("Choose the Loan Duration",0,20)
cibil_score = st.slider("Choose the cibil Score",0,1000)
total_asset_val = st.slider("Choose Asset",0,10000000)

## the education and self_emply is a string so we have to convert it into a number.
# education is converted in numeric value
if education == "Graduate":
    education_s = 1;
else:
    education_s = 0;
#self_emply is converted in numeric value
if self_emply == "Yes":
    self_emply_s = 1;
else:
    self_emply_s = 0;


# if the user will click the button predict it will predict the data-
if st.button("Predict"):
    pred_data = pd.DataFrame([[no_of_dependt, 
                               education_s,
                               self_emply_s,
                               income_annum,
                               loan_ammount,
                               loan_duration,
                               cibil_score,
                               total_asset_val]],
                               columns=
                         ['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score'	,'total_asset_value'])
    
    

    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)

    print(predict)

    if predict[0] == 1:
        st.success("The Loan is Approved");
    else:
        st.error("The loan is not Approved");