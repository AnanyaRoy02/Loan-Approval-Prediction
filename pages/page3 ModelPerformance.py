import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pickle as pk

#this is the trained model but for model performance we need x_test and y_pred also ... so we need train_test_split.

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

model = pk.load(open("model.pkl","rb"))  
scaler = pk.load(open("scaler.pkl","rb"))

df = pd.read_csv("loan_approval_dataset.csv")

# converting the string data into numerical data
df.columns = df.columns.str.strip()  # removing the extra space.

df["education"]=df["education"].replace([" Graduate"," Not Graduate"],[1,0])
df["self_employed"]=df["self_employed"].replace([" Yes"," No"],[1,0])
df["loan_status"]=df["loan_status"].replace([" Approved"," Rejected"],[1,0])


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_curve

df["total_asset_value"] = df["residential_assets_value"]+ df["commercial_assets_value"]+df["luxury_assets_value"]+df["bank_asset_value"]
df.drop(columns=["residential_assets_value" , "commercial_assets_value","luxury_assets_value","bank_asset_value"],inplace=True)

df.drop(columns=["loan_id"],inplace=True)

x = df.drop(["loan_status"],axis=1)  #all the independent variable
y = df["loan_status"]  #dependent variable



x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42) 

# scaling the independent variables

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

y_pred = model.predict(x_test_scaled)  # pred the test dataset

st.title("📊 Model Performance")

# Accuracy scoreee
st.subheader("1. Model Accuracy")
accuracy = accuracy_score(y_test,y_pred)
st.success(f"Accuracy: {accuracy*100:.2f}")

#Confusion matrix.
st.subheader("2. Confusion Matrix")
cm = confusion_matrix(y_test,y_pred)

fig,ax = plt.subplots(figsize=(10,8))
sns.heatmap(cm,annot=True,cmap="Reds",ax=ax)

ax.set_title("Confusion Matrix")
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")

st.pyplot(fig)

#classification Report - in a table format in streamlit.
st.subheader("3. Classification Report")
report = classification_report(y_test, y_pred, output_dict=True)

report_df = pd.DataFrame(report).transpose()

st.dataframe(report_df)

#number of correct and incorrect predictions
st.subheader("4. Prediction Summary")
st.text("This is the number of Correct and Incorrect Predictions.")

correct = (y_test == y_pred).sum()
incorrect = (y_test != y_pred).sum()

st.write(f"✅ Correct Predictions: {correct}") 
st.write(f"❌ Incorrect Predictions: {incorrect}") 
st.write(f"📊 Total Test Samples: {len(y_test)}")
