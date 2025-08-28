import streamlit as st
import pickle


with open("destree_model.sav", "rb") as f:
    nb = pickle.load(f)

st.title("📩 SMS Spam Classifier")
st.write("Enter values to predict whether an SMS is **Spam (1)** or **Not Spam (0)**")

word_freq_free = st.number_input("Word Frequency (free)", min_value=0.0, max_value=10.0, step=0.1)
word_freq_win = st.number_input("Word Frequency (win)", min_value=0.0, max_value=10.0, step=0.1)
word_freq_offer = st.number_input("Word Frequency (offer)", min_value=0.0, max_value=10.0, step=0.1)
sms_length = st.number_input("SMS Length", min_value=1, max_value=1000, step=1)


if st.button("Predict"):
    new_sms = np.array([[word_freq_free, word_freq_win, word_freq_offer, sms_length]])
    prediction = nb.predict(new_sms)[0]
    
    if prediction == 1:
        st.error("🚨 This SMS is predicted as **Spam**!")
    else:
        st.success("✅ This SMS is predicted as **Not Spam**.")
