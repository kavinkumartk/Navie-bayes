# 📩 SMS Spam Classifier

A Machine Learning project that predicts whether an SMS message is **Spam (1)** or **Not Spam (0)**.  
The project uses classical ML algorithms (**Naive Bayes** / **Decision Tree**) and provides an interactive frontend built with **Streamlit**.

---

## 🚀 Features
- Preprocess SMS dataset into numeric features
- Train & evaluate ML models
- Save and load trained models using `pickle`
- Interactive **Streamlit app** for end-user prediction
- Simple UI to enter SMS-related features and get prediction in real-time

---

## 📊 Dataset

We use a processed dataset (`spam.csv` → `df_features.csv`) with the following features:

| Feature            | Description                               |
|--------------------|-------------------------------------------|
| `word_freq_free`   | Frequency of the word "free" in SMS       |
| `word_freq_win`    | Frequency of the word "win" in SMS        |
| `word_freq_offer`  | Frequency of the word "offer" in SMS      |
| `sms_length`       | Length of the SMS (number of characters)  |
| `is_spam`          | Target variable (1 = Spam, 0 = Not Spam)  |

---

## 🛠️ Installation

Clone the repository:

git clone https://github.com/kavinkumartk/Navie-bayes

---

## 👨‍💻 Author
**Kavin Kumar T**
GitHub:  https://github.com/kavinkumartk

---