# 💉 Medical Insurance Cost Prediction (Gradient Descent + Streamlit)

This project is an end-to-end **Machine Learning regression application** that predicts **medical insurance charges** based on user details such as age, BMI, number of children, smoking habits, gender, and region.

The model is implemented using **Linear Regression from scratch** with **Gradient Descent optimization**, and deployed locally using **Streamlit** for real-time predictions through an interactive web interface.

---

## 🚀 Features

- Cleaned and processed the Kaggle Insurance dataset
- Implemented **Linear Regression from scratch**
- Optimized parameters using **Gradient Descent**
- Encoded categorical features using custom **target mean encoding**
- Evaluated model using **MAE, MSE, and R² Score**
- Built a **Streamlit web app** for prediction
- Saved trained model parameters using **Joblib** for reuse

---

## 📌 Dataset

Dataset used: **Insurance Dataset (Kaggle)**  
Contains 1338 records with the following features:

- age
- sex
- bmi
- children
- smoker
- region
- charges (target variable)

---

## 🧠 Machine Learning Approach

### 🔹 Model Used
- Linear Regression (implemented manually)

### 🔹 Optimization
- Gradient Descent (50,000 iterations)

### 🔹 Metrics Achieved
- **R² Score:** ~0.68  
- **MAE:** ~4715  
- **MSE:** ~46,724,888  

---

## ⚙️ Tech Stack

- Python
- Pandas, NumPy
- Matplotlib
- Joblib
- Streamlit

---

## 📂 Project Structure
Medical_insurance_prediction/\
│── app.py\
│── insurance.ipynb\
│── dataset/\
│ └── insurance.csv\
│── theta_final.pkl\
│── model_columns.pkl\
│── label_encodings.pkl\
│── requirements.txt\
│── README.md\


---

## 🖥️ Running the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AnanyaChattarjee/Medical_insurance_prediction.git
```
```
cd Medical_insurance_prediction
```
---
## 2️⃣ Install Required Libraries
```
./lib_install.sh
```

## 3️⃣ Run Streamlit App
```
streamlit run app.py
```

Then open in browser:
```
http://localhost:8501
```

## 📦 Model Files

The following files are generated after training:

- `theta_final.pkl` → learned weights (θ values)  
- `model_columns.pkl` → correct feature order  
- `label_encodings.pkl` → encoding mappings for categorical columns  

These are loaded directly inside the Streamlit app for predictions.

---

## 🎯 Streamlit Web App

The Streamlit app takes user inputs and predicts medical insurance charges instantly.

---

**Inputs include:**
- Age  
- BMI  
- Children  
- Sex  
- Smoker status  
- Region  

**Output:**
- Predicted insurance cost (charges)

---

## 📊 Visualization

A cost function convergence plot is generated to show how Gradient Descent minimizes loss over iterations.

---

## 🔗 GitHub Repository

📌 Project Link:  
[Medical Insurance Cost Prediction](https://github.com/AnanyaChattarjee/Medical_insurance_prediction)

---

## 👩‍💻 Author

**Ananya Chattarjee**  
📍 Jaipur, Rajasthan, India  
🔗 [LinkedIn](https://www.linkedin.com/in/ananya-chattarjee-669163275/)  
💻 [GitHub](https://github.com/AnanyaChattarjee)

