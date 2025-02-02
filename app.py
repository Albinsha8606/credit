import pickle
import streamlit as st
import numpy as np

st.title("Credit Card Fraud Detection App")

# Load the trained Random Forest model from the pickle file
file_name = "best_random_forest_model.pkl"
with open('best_random_forest_model.pkl', 'rb') as file:
 best_random_forest_model = pickle.load(file)

# Input fields for user to provide transaction details
st.header("Enter Transaction Details:")
time = st.number_input("Time (seconds since first transaction)", min_value=0)
amount = st.number_input("Transaction Amount ($)", min_value=0.0)

# Input fields for PCA components V1 to V28
pca_values = []
for i in range(1, 29):
    pca_values.append(st.number_input(f"V{i}", format="%.5f"))

# Button to trigger prediction
if st.button("Detect Fraud"):
    # Prepare the input data
    input_features = np.array([[time] + pca_values + [amount]])


    # Make prediction
    prediction = best_random_forest_model.predict(input_features)

    # Display the prediction
    if prediction[0] == 0:
        st.success("This transaction is predicted to be legitimate.")
    if prediction[0] == 1:    
        st.error("Warning: This transaction is predicted to be fraudulent.")
    