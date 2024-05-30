# Project Name

## Description

This project aims to predict house prices in New York City using a comprehensive dataset sourced from Kaggle. The dataset can be found [here](https://www.kaggle.com/datasets/nelgiriyewithana/new-york-housing-market). By leveraging machine learning techniques, this project provides insights into the factors that influence house prices and predicts future prices with high accuracy.

The project utilizes various Python libraries to process and analyze the data:
- **NumPy**: For efficient numerical operations and handling of arrays.
- **Pandas**: For data manipulation and analysis, providing data structures like DataFrames.
- **Matplotlib**: For data visualization, enabling the creation of plots and charts to illustrate data patterns and model performance.
- **Scikit-Learn (sklearn)**: For implementing machine learning algorithms, including data preprocessing, model training, and evaluation.
- **XGBoost**: An optimized gradient boosting library designed for performance and speed, used for building and fine-tuning the predictive model.

The dataset includes various features such as the number of bedrooms, bathrooms, square footage, location, and other relevant factors that influence house prices. By exploring and analyzing these features, the project aims to uncover patterns and relationships within the data, ultimately leading to accurate price predictions.

This project is a valuable tool for real estate agents, homebuyers, and investors who want to make informed decisions based on data-driven insights. It showcases the application of advanced machine learning techniques to solve real-world problems and provides a foundation for further enhancements and customization.
## Table of Contents
- [Project Name](#project-name)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Overview](#overview)
    - [Client](#client)
    - [Model](#model)
    - [Server](#server)
  - [Usage](#usage)
  - [Features](#features)
  - [Contact](#contact)

## Installation
Make sure you have Python 3.7 or higher installed on your machine. Clone the repository and install the required packages using the following commands:
```bash
git clone https://github.com/AlvaUtec/NY-Price-Prediction.git
cd NY-Price-Prediction
pip install -r requirements.txt
```

## Overview

The repository is structured into three main directories: `Client`, `Model`, and `Server`.

### Client
The `Client` directory contains everything related to the view of the HTML page. It includes:
- **CSS file**: Styles for the HTML page.
- **JS file**: JavaScript code for client-side interactions.
- **HTML file**: The main HTML page.

This directory uses only plain JavaScript and no frameworks, so it is straightforward and minimal.

### Model
The `Model` directory is divided into two parts: `datasets` and `model_creation`.

- **datasets**: Contains the raw dataset used for the project and the cleaned dataset after preprocessing.
- **model_creation**: Includes Jupyter Notebooks used for data cleaning, testing different models, and selecting the best model. The final model is saved as a pickle file for later use.

### Server
The `Server` directory includes the server and utility files needed to create the application. This directory handles:
- Setting up the server to communicate with the client.
- Loading the trained model.
- Receiving input parameters from the client, using the model to make predictions, and sending the results back to the client.

This structure ensures that the project is organized and each component is easy to locate and manage.


## Usage

If you only want to use the model, you need to install the required dependencies (explained in the Installation section above). Then, simply run the server and open the app in your browser:

1. Run the server:
    ```bash
    python server/server.py
    ```

2. Open the `app.html` file located in the `Client` directory in your browser.

3. Insert the parameters into the HTML form to get the predicted house price.

If you would like to explore how the model was constructed and where the data came from, you can take a look at the `Model` directory. This directory includes the dataset, data cleaning process, and model training steps in Jupyter Notebooks.

## Features

- **User-Friendly Interface**: Simple and intuitive HTML page for inputting house parameters and displaying predictions.
- **Accurate Predictions**: Utilizes advanced machine learning algorithms to provide accurate house price predictions.
- **Data Visualization**: Includes visualizations to help understand the data and model performance (available in the Jupyter Notebooks in the Model directory).
- **Comprehensive Data Processing**: Thorough data cleaning and preprocessing to ensure the quality of the input data.
- **Model Testing and Selection**: Evaluation and comparison of multiple models to select the best-performing one.
- **Saved Model**: The final model is saved as a pickle file for easy loading and use in the server application.
- **Modular Code Structure**: Clear separation of client-side, model, and server-side code for better organization and maintainability.


## Contact

If you have any questions, suggestions, or would like to contribute to the project, feel free to reach out:

- **Email**: alvaro.garcia.h@utec.edu.pe
- **LinkedIn**: [Alvaro Garcia Hurtado](https://www.linkedin.com/in/alvaro-garc%C3%ADa-hurtado-5901212a6/)

I'll appreciate your feedback and your interest. Thank you for checking out this project!
