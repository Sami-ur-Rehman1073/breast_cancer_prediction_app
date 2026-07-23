# 🩺 Breast Cancer Prediction API

A beginner-friendly yet production-inspired **FastAPI** web application that serves a trained machine learning model for breast cancer prediction. The application provides a clean web interface where users can enter all **30 diagnostic features** from the Breast Cancer Wisconsin (Diagnostic) dataset, receive an instant prediction, and store every prediction in a **MySQL** database for future reference.

The project focuses on demonstrating a complete machine learning deployment workflow, including model serving, web development, database integration, and prediction history management while keeping the codebase simple, readable, and easy to understand.

---

# 📌 Project Overview

Machine learning models are only useful when they can be deployed and used by end users. This project demonstrates how a trained Scikit-learn pipeline can be integrated into a FastAPI application without including any model training code.

The application:

* Loads a previously trained machine learning pipeline.
* Accepts user input through a web form.
* Performs inference using the trained model.
* Stores prediction results along with all feature values.
* Displays prediction history from a MySQL database.

The training and preprocessing pipeline are intentionally kept separate from the deployment project. The API only performs inference using the saved pipeline.

---

# ✨ Features

* FastAPI-based web application
* Simple and responsive frontend using Tailwind CSS
* Prediction using a pre-trained Scikit-learn pipeline
* Support for all 30 Breast Cancer Wisconsin dataset features
* Automatic loading of trained model
* MySQL database integration
* Stores every prediction made through the application
* View complete prediction history
* SQLAlchemy ORM
* Pydantic request validation
* Beginner-friendly folder structure
* Minimal and readable code

---

# 🧠 Machine Learning Workflow

The deployed model was trained separately using a complete machine learning pipeline.

Training workflow:

1. Data Exploration (EDA)
2. Train/Test Split
3. Feature Scaling using ColumnTransformer
4. Class Imbalance Handling
5. Pipeline Creation
6. Model Training
7. Cross Validation
8. Hyperparameter Tuning
9. Model Evaluation
10. Save Trained Pipeline using Joblib

The deployment project only loads the saved pipeline for prediction.

---

# 🏗 Project Structure

```text
breast_cancer_prediction_api/
│
├── trained_models/
│   └── selected_model.pkl
│
├── templates/
│   ├── index.html
│   └── history.html
│
├── app.py
├── config.py
├── crud.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

# ⚙️ Technologies Used

## Backend

* FastAPI
* Python
* Uvicorn

## Machine Learning

* Scikit-learn
* Joblib
* Pandas
* NumPy

## Database

* MySQL
* SQLAlchemy
* PyMySQL

## Frontend

* HTML
* Jinja2 Templates
* Tailwind CSS

---

# 📊 Input Features

The application accepts all **30 diagnostic features** used by the Breast Cancer Wisconsin (Diagnostic) dataset.

### Mean Features

* Mean Radius
* Mean Texture
* Mean Perimeter
* Mean Area
* Mean Smoothness
* Mean Compactness
* Mean Concavity
* Mean Concave Points
* Mean Symmetry
* Mean Fractal Dimension

### Standard Error Features

* Radius Error
* Texture Error
* Perimeter Error
* Area Error
* Smoothness Error
* Compactness Error
* Concavity Error
* Concave Points Error
* Symmetry Error
* Fractal Dimension Error

### Worst Features

* Worst Radius
* Worst Texture
* Worst Perimeter
* Worst Area
* Worst Smoothness
* Worst Compactness
* Worst Concavity
* Worst Concave Points
* Worst Symmetry
* Worst Fractal Dimension

---

# 🗄 Database

The application stores every prediction made by the user.

Each record contains:

* All 30 input features
* Prediction result
* Timestamp

This allows users to review previous predictions from the History page.

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/breast_cancer_prediction_api.git

cd breast_cancer_prediction_api
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🛢 Configure MySQL

Create a database.

```sql
CREATE DATABASE breast_cancer_db;
```

Update your `.env` or `config.py` with your database credentials.

Example:

```text
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=breast_cancer_db
```

When the application starts, SQLAlchemy automatically creates the required tables if they do not already exist.

---

# 🤖 Add Trained Model

Place your trained pipeline inside:

```text
trained_models/
```

Example:

```text
trained_models/
    selected_model.pkl
```

The application loads this model automatically during startup.

---

# ▶️ Run the Application

```bash
uvicorn app:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 💻 Application Workflow

```text
User

↓

HTML Form

↓

FastAPI

↓

Validate Input

↓

Convert to DataFrame

↓

Load Trained Pipeline

↓

Predict

↓

Save to MySQL

↓

Return Prediction

↓

View History
```

---

# 📈 Prediction History

Every prediction is saved automatically.

The History page displays:

* Prediction
* Date & Time
* All 30 feature values

This provides a simple audit trail of previous predictions.

---

# 🎯 Learning Objectives

This project demonstrates:

* Machine Learning Model Deployment
* FastAPI Fundamentals
* SQLAlchemy ORM
* Database CRUD Operations
* HTML Form Handling
* Jinja2 Templates
* Tailwind CSS Integration
* Loading Pre-trained ML Models
* Model Inference
* Project Organization
* Backend Development

---

# 📌 Future Improvements

Possible future enhancements include:

* User authentication
* Input validation messages
* Prediction probability display
* Confidence score visualization
* REST API endpoints for external clients
* Pagination for prediction history
* Search and filtering
* Docker containerization
* Cloud deployment
* Logging and monitoring
* Unit and integration tests

---


