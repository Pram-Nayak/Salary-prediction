#Salary Predictor

## Overview
A machine learning model deployed with Flask API to predict data science salaries based on various job features. The model analyzes multiple factors including company rating, years of experience, and job-specific characteristics to estimate annual salaries.


<img src="https://drive.google.com/uc?id=1E6-ZAASuX9l7Bw5aHUhhX-EFw5MRGa6C" alt="Home Page" width="600">


## Features
- **Web Interface**: User-friendly interface for salary predictions
- **REST API**: Endpoint for programmatic access
- **ML Model**: Random Forest Regressor trained on real job market data
- **Input Features**:
  - Company Rating (0-5)
  - Years of Experience
  - Job Description Length
  - Binary indicators for:
    - Skills (Python, AWS, etc.)
    - Location
    - Company Type
    - Other job-related features


### Web Interface
1. Navigate to `http://127.0.0.1:5000`
2. Input the required features in comma-separated format
3. Click "Get Prediction"
4. View the predicted salary



## Model Details
- **Algorithm**: Random Forest Regressor
- **Features**: 177 input features
- **Output**: Predicted annual salary in thousands (USD)
- **Example**: Output of 51.24 represents $51,240



