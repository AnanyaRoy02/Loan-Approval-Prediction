import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Dataset Analysis")
df =pd.read_csv("loan_approval_dataset.csv")

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

# Distribution of cibil score with histogram.

st.subheader("1. Distribution of CIBIL Score")

fig,ax = plt.subplots(figsize=(10,5))
st.write("""
This graph shows the distribution of applicants based on their CIBIL scores.
A higher CIBIL score generally indicates better creditworthiness.
""")
ax.hist(
    df[" cibil_score"],
    bins=20,
    edgecolor="black",
    )

ax.set_xlabel("CIBIL Score")
ax.set_ylabel("No. of Applicants")
ax.set_title("Distribution of Cibil score")

st.pyplot(fig)


# Distribution  of income in bar plot

st.subheader("2. Loan status")   # bar plot
st.write("This graph shows the loan status of applicants.")
fig,ax = plt.subplots(figsize=(10,5))

# ax.bar(df[" loan_status"],
#        color=["green","red"])
df[" loan_status"].value_counts().plot(
    kind="bar",
    color=["green","red"],
    ax=ax
)
ax.set_xlabel("Loan Status")
ax.set_ylabel("No. of Applicants")
ax.set_title("Approved vs Rejected Loans")
st.pyplot(fig)

# Distribution of Annual Income
st.subheader("3. Distribution of Annual Income")

st.write()
fig,ax = plt.subplots(figsize=(10,5))
ax.hist(df[" income_annum"],bins=20,edgecolor="black",color="yellow")

ax.set_xlabel("Annual Income")
ax.set_ylabel("No. of Applicants")
ax.set_title("Distribution of Annual Income")

st.pyplot(fig)


#Distribution of Income vs loan account - scatter plot

st.subheader("4. Income vs Loan Account")
fig, ax =  plt.subplots(figsize=(10,5))
ax.scatter(df[ " income_annum"],df[ " loan_amount"],color=["blue"])
ax.set_title("Income VS Loan Amount")
ax.set_xlabel("Annual Income")
ax.set_ylabel("Loan Amount")
st.pyplot(fig)

#Correlation heatmap for all numerical values
st.subheader("5. Correlation Heatmap")

fig,ax = plt.subplots(figsize=(10,8))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    color="blue",
    ax=ax
)
st.pyplot(fig)