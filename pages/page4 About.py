import streamlit as st 
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



st.title("ℹ️ About the Project")

st.header("Loan Approval Prediction System")

st.write("""
The Loan Approval Prediction System is a Machine Learning based web application
that predicts whether a loan application is likely to be approved or rejected.
The prediction is based on important applicant details such as annual income,
loan amount, loan term, CIBIL score, education, employment status, dependents,
and total asset value.

The project is developed using the Logistic Regression algorithm and deployed
using Streamlit to provide a simple and interactive user interface.
""")

st.header("Project Objectives")

st.markdown("""
- Predict loan approval using Machine Learning.
- Reduce manual effort in loan evaluation.
- Help users understand the factors affecting loan approval.
- Visualize the dataset using different graphs.
- Evaluate the model using performance metrics.
""")

st.header("Technologies Used")

st.markdown("""
- **Programming Language:** Python
- **Machine Learning:** Scikit-learn (Logistic Regression)
- **Data Processing:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Web Framework:** Streamlit
- **Model Saving:** Pickle
""")

st.header("Application Features")

st.markdown("""
- 🏠 Home Page
- 🤖 Loan Approval Prediction
- 📊 Dataset Analysis
- 📈 Model Performance Evaluation
- ℹ️ About Project
""")

st.header("Model Evaluation")

st.markdown("""
The model performance is evaluated using:
- Accuracy Score
- Confusion Matrix
- Classification Report
- Prediction Summary
""")

st.header("Future Enhancements")

st.markdown("""
- Deploy the application online.
- Compare multiple Machine Learning algorithms.
- Improve prediction accuracy using feature engineering.
- Connect the application with a database.
- Add user authentication and login.
""")

st.success("Thank you for exploring the Loan Approval Prediction System! 🚀")