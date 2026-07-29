import streamlit as st

st.set_page_config(page_title= "Loan Approval Prediction")

st.title("🏠Home Page")
st.subheader("Welcome to Loan Approval Prediction system")
st.write("This app uses machine learning to quickly predict if a loan should be approved. It securely checks the applicant's income, credit history, and details to give a fast, reliable decision.")

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

# Step-by-Step Navigation Guide
st.subheader("🚀 Get Started")

col1, col2 = st.columns(2)

with col1:
    st.markdown("##### 1. Analyze Data")
    st.write("Review historical distributions and correlations.")
    if st.button("Go to Dataset Analysis", use_container_width=True):
        st.info("Please select 'page2 Dataset Analysis' from the sidebar.")

with col2:
    st.markdown("##### 2. Run Predictions")
    st.write("Input financial metrics to test eligibility.")
    if st.button("Go to Loan Prediction", use_container_width=True):
        st.info("Please select 'page1 LoanPrediction' from the sidebar.")

col1,col2 = st.columns(2)
with col1:
    st.markdown("##### 3. Model Performance")
    st.write("Model Performance in the dataset.")
    if st.button("Go to Model Performance", use_container_width=True):
        st.info("Please select 'page3 ModelPerformance' from the sidebar.")

with col2:
    st.markdown("##### 4. About the Project")
    st.write("It is the Description about the project")
    if st.button("Go to About", use_container_width=True):
        st.info("Please select 'page4 About' from the sidebar.")