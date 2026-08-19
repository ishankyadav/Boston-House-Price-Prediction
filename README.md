# 🏠 Boston House Price Prediction

A machine learning web application that predicts Boston house prices based on property and socioeconomic features.

The project uses regression algorithms trained on the Boston Housing dataset and provides an interactive prediction interface built with **Streamlit**.

---

## 🚀 Live Demo

🔗 **Streamlit App:** https://boston-house-price-prediction-jdwrorcbea8xluxmhkco7u.streamlit.app/

---

## 📌 Project Overview

House price prediction is a regression problem in which machine learning models learn the relationship between housing characteristics and their corresponding property values.

In this project, multiple regression algorithms were trained and evaluated to identify a suitable model for predicting house prices.

The final trained model is integrated into a Streamlit web application where users can enter property characteristics and receive an estimated house price.

---

## 🎯 Objectives

* Build a machine learning model for house price prediction.
* Perform exploratory data analysis on the housing dataset.
* Handle missing values using preprocessing techniques.
* Compare multiple regression algorithms.
* Evaluate models using MAE, RMSE, and R² Score.
* Save the trained model using Joblib.
* Build an interactive Streamlit frontend.
* Deploy the application using Streamlit Community Cloud.

---

## 🧠 Machine Learning Workflow

```text
Housing Dataset
       ↓
Data Exploration
       ↓
Missing Value Analysis
       ↓
Feature / Target Separation
       ↓
Train-Test Split
       ↓
Data Preprocessing
       ↓
Model Training
       ↓
Model Comparison
       ↓
Best Model Selection
       ↓
Model Evaluation
       ↓
Model Serialization
       ↓
Streamlit Application
       ↓
Cloud Deployment
```

---

## 📊 Dataset

The dataset contains **506 observations** and **14 columns**.

There are **13 input features** and one target variable:

### Target Variable

**MEDV**

`MEDV` represents the median value of owner-occupied homes and is expressed in thousands of dollars.

### Input Features

| Feature | Description                                          |
| ------- | ---------------------------------------------------- |
| CRIM    | Per capita crime rate by town                        |
| ZN      | Proportion of residential land zoned for large lots  |
| INDUS   | Proportion of non-retail business acres              |
| CHAS    | Charles River dummy variable                         |
| NOX     | Nitric oxide concentration                           |
| RM      | Average number of rooms per dwelling                 |
| AGE     | Proportion of owner-occupied units built before 1940 |
| DIS     | Weighted distance to employment centers              |
| RAD     | Accessibility to radial highways                     |
| TAX     | Property-tax rate                                    |
| PTRATIO | Pupil-teacher ratio                                  |
| B       | Population-related feature                           |
| LSTAT   | Percentage of lower-status population                |

---

## 🤖 Models Evaluated

The following regression algorithms were compared:

1. Linear Regression
2. Ridge Regression
3. Random Forest Regressor
4. Gradient Boosting Regressor
5. Extra Trees Regressor

The final model is selected automatically based on the highest **R² Score** on the test set.

---

## 📈 Evaluation Metrics

The project uses three primary evaluation metrics:

### Mean Absolute Error — MAE

Measures the average absolute difference between actual and predicted values.

Lower MAE indicates better performance.

### Root Mean Squared Error — RMSE

Measures the square root of the average squared prediction error.

Lower RMSE indicates better performance.

### R² Score

Measures how well the model explains the variation in the target variable.

A value closer to 1 indicates better predictive performance.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* NumPy
* Pandas

### Model Persistence

* Joblib

### Visualization

* Matplotlib
* Seaborn

### Frontend

* Streamlit

### Deployment

* Streamlit Community Cloud

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
Boston-House-Price-Prediction/
│
├── app.py
│
├── boston_house_price_model.pkl
│
├── feature_names.pkl
│
├── model_metadata.pkl
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Boston-House-Price-Prediction.git
```

### 2. Navigate to the project

```bash
cd Boston-House-Price-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

#### Windows CMD

```bash
.venv\Scripts\activate.bat
```

#### Windows PowerShell

If PowerShell blocks script execution, you can directly use the environment's Python executable instead.

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Streamlit

```bash
python -m streamlit run app.py
```

The application will open locally at:

```text
http://localhost:8501
```

---

## 🌐 Deployment

This application can be deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the repository.
5. Select the `main` branch.
6. Set `app.py` as the main file.
7. Deploy the application.

Streamlit Community Cloud automatically installs the Python dependencies specified in `requirements.txt`.

---

## 🔮 How the Application Works

The user enters values for the 13 housing features.

The Streamlit application creates a Pandas DataFrame from these values and passes it to the trained machine learning pipeline.

```text
User Input
    ↓
13 Housing Features
    ↓
Pandas DataFrame
    ↓
Saved ML Pipeline
    ↓
Prediction
    ↓
Estimated House Price
```

The trained model is loaded using Joblib:

```python
model = joblib.load("boston_house_price_model.pkl")
```

---

## ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes**.

The predicted house price is an estimate generated by a machine learning model and should not be considered a real-world property valuation.

---

## 👨‍💻 Author

**Ishank Yadav**

B.Tech — Computer Science & Engineering
Specialization: Artificial Intelligence & Machine Learning

---

## ⭐ If You Like This Project

If you found this project useful, consider giving the repository a ⭐ on GitHub.
