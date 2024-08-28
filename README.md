# Car Price Prediction Project

This project is a web application designed to predict car prices based on various input features using machine learning models. The application is developed using FastAPI for the API framework and Scikit-learn for model training and evaluation.

## Features

- Provides car price predictions based on user-provided features.
- Exposes a REST API using FastAPI for seamless integration.
- Utilizes multiple machine learning models to enhance prediction accuracy.

## Requirements

- Python 3.7 or higher
- FastAPI
- Uvicorn
- Pandas
- NumPy
- Scikit-learn

## Project Workflow

1. **Data Collection and Preprocessing**: Collect and preprocess data, including features such as car model, year, mileage, engine size, and other relevant attributes. Handle missing values and encode categorical data.
2. **Model Training**: Train various machine learning models using the Scikit-learn library. Evaluate models using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared values to determine the best-performing model.
3. **API Development**: Develop RESTful API endpoints using FastAPI to serve the model predictions. Implement endpoints for predicting car prices and retrieving model details.
4. **Testing**: Perform unit and integration testing to ensure the API is functioning as expected and that the model predictions are accurate.
5. **Deployment**: Deploy the FastAPI application using Uvicorn. The API will be accessible via a web server for user interaction and integration with other applications.

## Usage

- Start the FastAPI server to access the application.
- Use the `/predict` endpoint to send a POST request with car feature details to receive a price prediction.
- Example request:

    ```json
    {
        "model": "Toyota Camry",
        "year": 2019,
        "mileage": 30000,
        "engine_size": 2.5,
        "fuel_type": "Petrol",
        "transmission": "Automatic"
    }
    ```

- The response will include the predicted price based on the provided car features.

## Acknowledgements

- Special thanks to all contributors and the open-source community for the libraries and tools used in this project.

